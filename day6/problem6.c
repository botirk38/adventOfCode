#include <stdio.h>

int calculate_ways(int total_time, int record_distance) {
    int ways = 0;
    for (int t = 1; t < total_time; ++t) {
        int distance = t * (total_time - t);
        if (distance > record_distance) {
            ++ways;
        }
    }
    return ways;
}

int main() {
    FILE *file = fopen("test.txt", "r");
    if (file == NULL) {
        perror("Error opening the file");
        return 1;
    }

    int times[4];
    int distances[4];

    // Skip the label "Time:"
    fscanf(file, "%*s");

    // Read times
    for (int i = 0; i < 4; ++i) {
        if (fscanf(file, "%d", &times[i]) != 1) {
            fprintf(stderr, "Error reading time %d from file\n", i + 1);
            fclose(file);
            return 1;
        }
    }

    // Skip the label "Distance:"
    fscanf(file, "%*s");

    // Read distances
    for (int i = 0; i < 4; ++i) {
        if (fscanf(file, "%d", &distances[i]) != 1) {
            fprintf(stderr, "Error reading distance %d from file\n", i + 1);
            fclose(file);
            return 1;
        }
    }

    fclose(file);

    int total_ways = 1;

    for (int i = 0; i < 4; ++i) {
        int ways = calculate_ways(times[i], distances[i]);
        total_ways *= ways;
        printf("Race %d: %d ways to win\n", i + 1, ways);
    }

    printf("Total ways to win all races: %d\n", total_ways);
    return 0;
}

