
// https://leetcode.com/problems/print-in-order/

class Foo {
public:
    Foo(): work_n(0) {
        
    }
    
    atomic_int work_n;
    std::mutex m;
    std::condition_variable cv;

    void first(function<void()> printFirst) {
        std::unique_lock<std::mutex> lock(m);
        cv.wait(lock, [this]{return work_n == 0;});
        
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        work_n++;
        
        lock.unlock();
        cv.notify_all();
    }

    void second(function<void()> printSecond) {
        std::unique_lock<std::mutex> lock(m);
        cv.wait(lock, [this]{return work_n == 1;});
        
        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        work_n++;
        
        lock.unlock();
        cv.notify_all();
    }

    void third(function<void()> printThird) {
        std::unique_lock<std::mutex> lock(m);
        cv.wait(lock, [this]{return work_n == 2;});
        
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
        work_n++;
        
        lock.unlock();
        cv.notify_all();
    }
};