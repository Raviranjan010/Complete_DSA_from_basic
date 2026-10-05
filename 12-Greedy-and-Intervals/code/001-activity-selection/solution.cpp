// Activity selection / Non-overlapping intervals in C++
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Activity {
    int start, finish;
};

bool compareActivities(const Activity& a, const Activity& b) {
    return a.finish < b.finish;
}

int maxActivities(vector<Activity>& activities) {
    if (activities.empty()) return 0;
    sort(activities.begin(), activities.end(), compareActivities);

    int count = 1;
    int lastFinish = activities[0].finish;

    for (size_t i = 1; i < activities.size(); i++) {
        if (activities[i].start >= lastFinish) {
            count++;
            lastFinish = activities[i].finish;
        }
    }
    return count;
}

int main() {
    vector<Activity> acts = {{1, 2}, {3, 4}, {0, 6}, {5, 7}, {8, 9}, {5, 9}};
    cout << "Maximum non-conflicting activities: " << maxActivities(acts) << endl;
    return 0;
}
