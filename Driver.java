class Driver{
	public static void main(String args[]){
		System.out.println("making objects");
		Employee e = new Employee(1, "Khuram Ahmad");
		System.out.println("making objects of Teacher class");
		Teacher t = new Teacher();
		Teacher t1 = new Teacher(2, "Ali Raza", "phd");

		e.display();
		t.display();
		t1.display();
		}
}















