class LinkedListNode{
public:
  int value_;
  LinkedListNode* next_;

  LinkedListNode(int value):
  value_(value);
  next_(nullptr){

  }
};





bool containCycle(const LinkedListNode* firstnode){
  const LinkedListNode* slow=firstnode;
  const LinkedListNode* fast=firstnode;


  while (fast!=nullptr && fast->next_){
    fast=fast->next_->next_;
    slow=slow->next_;


    if (fast==slow){
      return true;
    }
  }

  return false;
}
