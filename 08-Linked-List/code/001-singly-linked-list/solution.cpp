// Basic Singly Linked List operations in C++: insertion, traversal, and reversal
#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

void printList(ListNode* head) {
    ListNode* curr = head;
    while (curr) {
        cout << curr->val << (curr->next ? " -> " : "");
        curr = curr->next;
    }
    cout << endl;
}

ListNode* reverseList(ListNode* head) {
    ListNode* prev = nullptr;
    ListNode* curr = head;
    while (curr) {
        ListNode* nextNode = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nextNode;
    }
    return prev;
}

int main() {
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);

    cout << "Original list: ";
    printList(head);

    head = reverseList(head);
    cout << "Reversed list: ";
    printList(head);

    return 0;
}
