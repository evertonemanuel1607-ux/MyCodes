import java.util.ArrayList;
import java.util.Scanner;

class Student {
    private String name;
    private boolean result;

    Student(String name , boolean result) {
        this.name = name;
        this.result = false;
    }

    public String getName() {
        return name;
    }

    public String getResult() {
        if (result) {
            return "Approved";
        }
        else {
            return "Failed";
        }
    }

    public void setResult(String result) {
        if (result.equals("y")) {
            this.result = true;
            
        }
        else if (result.equals("n")) {
            this.result = false;

        }


    }
}

class School {
    private ArrayList<Student> class_school = new ArrayList<>();
    public void SetNew(Student student) {
        class_school.add(student);
    }
    public String SearchStudent(String name) {
        for(Student i : class_school) {
            if (i.getName().equals(name) ) {
                return i.getResult();
                
            }
        }
        return "Not Found";
    }


}