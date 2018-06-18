/**
 * @author liwei
 * @date 18/6/18 上午7:36
 */

class Student{
    private String name;
    private int age;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
}

public class Main {

    public static void main(String[] args) {
        Student s = null;
        hello(s);
        System.out.println(s==null);
    }

    private static void hello(Student s){
        if(s==null){
            s = new Student();
            s.setName("liwei");
            s.setAge(24);
        }
        System.out.println(s==null);
    }
}
