import java.util.ArrayList;
import java.util.Collections;
public class ArrayListExample {
    public static void main(String[] args) {
        ArrayList<MyClass> myList = new ArrayList<>();

        // Adding elements to the ArrayList
        myList.add(new MyClass(1, "John", 90.5));
        myList.add(new MyClass(2, "Emily", 85.2));
        myList.add(new MyClass(3, "Michael", 92.8));

        System.out.println("Elements in the ArrayList:");

        for (MyClass obj : myList) {
            System.out.println("ID: " + obj.getId() + ", Name: " + obj.getName() + ", Score: " + obj.getScore());
        }

        // Getting element at index 1
        MyClass element = myList.get(1);
        System.out.println("\nElement at index 1: ID: " + element.getId() + ", Name: " + element.getName() + ", Score: " + element.getScore());

        // Modifying element at index 2
        myList.set(2, new MyClass(3, "Sarah", 88.6));
        System.out.println("\nElements in the ArrayList after modification:");

        for (MyClass obj : myList) {
            System.out.println("ID: " + obj.getId() + ", Name: " + obj.getName() + ", Score: " + obj.getScore());
        }

        // Removing element at index 0
        myList.remove(0);
        System.out.println("\nElements in the ArrayList after removal:");

        for (MyClass obj : myList) {
            System.out.println("ID: " + obj.getId() + ", Name: " + obj.getName() + ", Score: " + obj.getScore());
        }

        // Clearing the ArrayList
        myList.clear();
        System.out.println("\nElements in the ArrayList after clearing: " + myList.size());

        // Sorting the ArrayList based on score
        myList.add(new MyClass(1, "John", 90.5));
        myList.add(new MyClass(2, "Emily", 85.2));
        myList.add(new MyClass(3, "Michael", 92.8));

        Collections.sort(myList, (o1, o2) -> Double.compare(o1.getScore(), o2.getScore()));
        System.out.println("\nElements in the ArrayList after sorting:");

        for (MyClass obj : myList) {
            System.out.println("ID: " + obj.getId() + ", Name: " + obj.getName() + ", Score: " + obj.getScore());
        }
    }
}