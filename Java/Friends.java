class Friends {
  public static void main(String arg[]){
		String X = “Book“;
		String Y = “Laptop”;
		String Z = “Mobile”;
		System.out.println(“Before Gifting : ”);
		System.out.println(“X has : ”+X);
    System.out.println(“Y has : ”+Y);
    System.out.println(“Z has : ”+Z);
    String tempX = X, tempY = Y, tempZ = Z;
		Y = tempX;
		Z = tempY;
		X = tempZ;
		System.out.println(“After Gifting : ”);
		System.out.println(“X has : ”+X);
    System.out.println(“Y has : ”+Y);
    System.out.println(“Z has : ”+Z);
  }
}
