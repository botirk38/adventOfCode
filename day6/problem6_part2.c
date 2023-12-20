#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long long int calculate_ways(long long int total_time, long long int record_distance) {
    long long int ways = 0;
    for (long long int t = 1; t < total_time; ++t) {
        long long int distance = t * (total_time - t);
        if (distance > record_distance) {
            ++ways;
        } else {
            // Debugging output
            printf("t: %lld, distance: %lld\n", t, distance);
        }
    }
    return ways;
}


int main() {
   

    long long int ways = calculate_ways(54946592, 302147610291404);
    printf("Ways to win the race: %lld\n", ways);

    return 0;
}

