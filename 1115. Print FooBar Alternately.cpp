
// https://leetcode.com/problems/print-foobar-alternately/

//// TTAS lock
// void lock() {
//     for (;;) {
//       if (!lock_.exchange(true, std::memory_order_acquire)) {
//         break;
//       }
//       while (lock_.load(std::memory_order_relaxed));
//     }
//   }

class FooBar {
private:
    int n;
    atomic<bool> is_foo;

public:
    FooBar(int n): is_foo(false) {
        this->n = n;
    }

    void foo(function<void()> printFoo) {
        
        for (int i = 0; i < n; i++) {
            for(;;) {
                if(!is_foo.exchange(true, memory_order_acquire)) break;
                while (is_foo.load(memory_order_relaxed));
            }
            
            printFoo();
        }
    }

    void bar(function<void()> printBar) {
        
        for (int i = 0; i < n; i++) {
            for(;;) {
                if(is_foo.exchange(false, memory_order_acquire)) break;
                while (!is_foo.load(memory_order_relaxed));
            }
            
            printBar();
        }
    }
};


