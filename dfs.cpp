
// https://www.hackerrank.com/challenges/pacman-dfs

#include <iostream>
#include <vector>
#include <stack>
#include <tuple>

using namespace std;

bool isVisited(const tuple<int, int>& node, vector<tuple<int, int>>& visited){
    // check if this node is already visited
    // TODO: optimize using r x c bool matrix
    vector<tuple<int, int>>::iterator it = visited.begin();
    for(; it != visited.end(); it++)
        if(*it == node)
            return true;
    return false;    
}


// r, c - grid size
// pacman_r, pacman_c - position of Pacman
// food_r, food_c - position of food
void dfs(int r, int c, int pacman_r, int pacman_c, int food_r, int food_c, vector <string> grid){
    
    stack<tuple<int, int>> S;
    S.push(make_tuple(pacman_r, pacman_c));
    
    // all nodes that were visited
    vector<tuple<int, int>> visited, explored;
    
    int nodes_explored = 0;
    
    // current vertex coordinates
    int v_r, v_c;
    tuple<int, int> v, t;
    while(!S.empty()) {
        // get a node from the stack
        v = S.top();
        S.pop();
        
        explored.push_back(v);
        nodes_explored++;
        
        // if wasn't visited
        if(!isVisited(v, visited)){
            // label as visited
            visited.push_back(v);
            
            // add ajacent nodes to stack
            tie(v_r, v_c) = v;
            
            // if found food
            if(v_r == food_r && v_c == food_c){
                break;
            }
            
            // up
            if(int(grid[v_r - 1][v_c]) != 37){
                t = make_tuple(v_r - 1, v_c);
                if(!isVisited(t, visited))
                    S.push(t);
            }
                        
            // left
            if(int(grid[v_r][v_c - 1]) != 37){
                t = make_tuple(v_r, v_c - 1);
                if(!isVisited(t, visited))
                    S.push(t);
            }
            
            // right
            if(int(grid[v_r][v_c + 1]) != 37){
                t = make_tuple(v_r, v_c + 1);
                if(!isVisited(t, visited))
                    S.push(t);
            }
            
            // down
            if(int(grid[v_r + 1][v_c]) != 37){
                t = make_tuple(v_r + 1, v_c);
                if(!isVisited(t, visited))
                    S.push(t);
            }      
        }
    }
    
    vector<tuple<int, int>>::iterator it;
    
    cout << visited.size() << endl;
    for(it = visited.begin(); it != visited.end(); it++){
        tie(v_r, v_c) = *it;
        cout << v_r << " " << v_c << endl;
    }
    
    cout << explored.size() - 1 << endl;
    for(it = explored.begin(); it != explored.end(); it++){
        tie(v_r, v_c) = *it;
        cout << v_r << " " << v_c << endl;
    }
        

}

int main(void) {

    int r,c, pacman_r, pacman_c, food_r, food_c;
    
    cin >> pacman_r >> pacman_c;
    cin >> food_r >> food_c;
    cin >> r >> c;
    
    vector <string> grid;

    for(int i=0; i<r; i++) {
        string s; cin >> s;
        grid.push_back(s);
    }

    dfs( r, c, pacman_r, pacman_c, food_r, food_c, grid);

    return 0;
}