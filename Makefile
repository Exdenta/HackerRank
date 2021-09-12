CC=g++

binary_search_array:
	$(CC) binary_search_array.cpp -o bin/binary_search_array

binary_search_tree:
	$(CC) binary_search_tree.cpp -o bin/binary_search_tree

bracket_seq_generator:
	$(CC) bracket_seq_generator.cpp -o bin/bracket_seq_generator

dijkstra:
	$(CC) dijkstra.cpp -o bin/dijkstra

sherlock_and_the_valid_string:
	$(CC) sherlock_and_the_valid_string.cpp -o bin/sherlock_and_the_valid_string

max_array_sum:
	$(CC) max_array_sum.cpp -o bin/max_array_sum

repeating_song_unordered_set:
	$(CC) repeating_song_unordered_set.cpp -o bin/repeating_song

two_sum_unordered_map:
	$(CC) two_sum_unordered_map.cpp -o bin/two_sum

functions_pipeline:
	$(CC) functions_pipeline.cpp -o bin/functions_pipeline

trees_alg:
	$(CC) -std=c++17 -g trees_alg.cpp -o bin/trees_alg