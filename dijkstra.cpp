#include <string>
#include <vector>
#include <tuple>
#include <iostream> 
#include <algorithm>    // std::any_of

std::tuple<std::vector<std::string>, std::vector<uint>> Dijkstra(std::vector<std::string> nodes, 
                                                                std::vector<std::vector<int>> edges, 
                                                                uint source);

int main(void)
{
    std::vector<std::string> nodes = {"A", "B", "C", "D", "E"};
    std::vector<std::vector<int>> edges = {{ 0, 6, -1,  1, -1},
                                           { 6, 0,  5,  2,  2},
                                           {-1, 5,  0, -1,  5},
                                           { 1, 2, -1,  0,  1},
                                           {-1, 2,  5,  1,  0}};   
    std::cout << nodes[0] << std::endl;
    uint source_idx_ = 0;

    std::vector<std::string> prev; 
    std::vector<uint> dist;
    tie(prev, dist) = Dijkstra(nodes, edges, source_idx_);

    // Print the results
    std::cout << "Prev nodes: [";
    for (std::string p : prev)
        std::cout << p << " ";
    std::cout << "]" << std::endl;
    std::cout << "Distances: [";
    for (uint d : dist)
        std::cout << d << " ";
    std::cout << "]" << std::endl;
    return 0;
}

std::tuple<std::vector<std::string>, std::vector<uint>> Dijkstra(std::vector<std::string> nodes, 
                                                                std::vector<std::vector<int>> edges, 
                                                                uint source) {
    // shortest path previous nodes
    std::vector<std::string> prev(nodes.size());
    std::vector<bool> visited(nodes.size());
    // shortest distances to every node
    std::vector<uint> dist(nodes.size());
    for(int i = 0; i < nodes.size(); i++) {
        prev[i] = "";
        visited[i] = false;
        dist[i] = UINT32_MAX;
    }
    dist[source] = 0;

    while(std::any_of(visited.begin(), visited.end(), [](bool e) {return !e;})){

        // find an unvisited node with the 
        // minimal distance from the source
        uint node_idx = 0;
        uint min_dist = UINT32_MAX;
        for(int i = 0; i < nodes.size(); i++){
            if(!visited[i] && dist[i] < min_dist){
                min_dist = dist[i];
                node_idx = i;
            }
        }

        // check if we have a shorter path to any node
        auto node_edges = edges[node_idx];
        for(int i = 0; i < nodes.size(); i++){
            if(node_edges[i] != -1){
                uint alt = node_edges[i] + dist[node_idx];
                if(alt < dist[i]){
                    dist[i] = alt;
                    prev[i] = nodes[node_idx];
                }
            }
        } 

        visited[node_idx] = true;
    }
    return std::make_tuple(prev, dist);
}
