import java.util.Iterator;
import java.util.NoSuchElementException;


public class DoubleList<E> implements Iterable<E> {

  private Link<E> head; // Pointer to list header
  private Link<E> tail; // Pointer to last node
  private int listSize; // Size of list

  /**
   * Create an empty LList.
   */

  DoubleList() {
    clear();
  }

  /**
   * Return the element at the provided index. This method will iterate from the
   * head or the tail depending on which will require fewer steps.
   */
  public E get(int pos) {
    if (pos < 0 || pos >= listSize) {
      throw new IndexOutOfBoundsException();
    }

    if (pos < listSize / 2) {
      return forward(pos).element();
    } else {
      return backward(pos).element();
    }
  }

  /**
   * Helper method for iterating forward from the head.
   */
  private Link<E> forward(int pos) {
    Link<E> current = head.next();
    for (int i = 0; i < pos; i++) {
      current = current.next();
    }
    return current;
  }

  /**
   * Helper method for iterating backward from the tail.
   */
  private Link<E> backward(int pos) {
    Link<E> current = tail.prev();
    for (int i = 0; i < (listSize - 1) - pos; i++) {
      current = current.prev();
    }
    return current;
  }

  /**
   * Remove the provided link from the list.
   */
  private void removeHelper(Link<E> link) {
    Link<E> prev = link.prev();
    Link<E> next = link.next();
    prev.setNext(link.next());
    next.setPrev(link.prev());
    listSize--;

  }

  /**
   * Return the number of elements stored in the list.
   */
  public int size() {
    return listSize;
  }
  



/**
   * Remove all elements in this list.
   */

  
  public void clear() {
    head = new Link<E>(null, null);
    tail = new Link<E>(head, null);
    head.setNext(tail);
    listSize = 0;
    
  }

  /**
   * Append item to the end of the list.
   */
  public void append(E item) {
    Link<E> new_node = new Link<E>(item, tail.prev(), tail);
    tail.prev().setNext(tail);
    tail.setPrev(new_node);
    tail.prev().prev().setNext(new_node);
    listSize++;
  }

  /**
   * Add the item at the specified index.
   */
  public void add(int index, E item) {
   Link<E> new_node = new Link<E>(item, forward(index-1), forward(index));
   forward(index).prev().setNext(forward(index));
   forward(index).setPrev(new_node);
  }

  /**
   * Remove and return the item at the specified index.
   */
  public E remove(int index) {
    E val = get(index);
    forward(index+1).setPrev(forward(index-1));
    forward(index-1).setNext(forward(index+1));
    return val;
  }

  /**
   * Reverse the list
   */
  public void reverse() {
    Link<E> curr = head; 
    Link<E> nextNode = head;
    Link<E> prevNode = head;  
    while (curr != null) {
      nextNode = curr.next();
      curr.setNext(prevNode);
      prevNode = curr;
      curr = nextNode;
    }   

  }


  /**
   * Iterates forward through the list. Remove operation is supported.
   */
  @Override
  public Iterator<E> iterator() {
    return new DoubleIterator();
  }
  
  private class DoubleIterator implements Iterator<E> {

    private Link<E> current;
    private boolean canRemove;

    public DoubleIterator() {
      current = head;
      canRemove = false;
    }

    @Override
    public boolean hasNext() {
      return current.next() != tail;
    }

    @Override
    public E next() {
      if (hasNext()) {
        current = current.next();
        canRemove = true;
        return current.element();
      } else {
        throw new NoSuchElementException();
      }
    }

    @Override
    public void remove() {
      if (!canRemove) {
        throw new IllegalStateException();
      }
      removeHelper(current);
      canRemove = false;
    }

  }

}
