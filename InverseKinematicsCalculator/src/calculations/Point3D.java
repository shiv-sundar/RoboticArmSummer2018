package calculations;

public class Point3D {
	double x;
	double y;
	double z;
	
	public Point3D() {
		this.x = 0;
		this.y = 0;
		this.z = 0;
	}
	
	public Point3D(double x, double y, double z) {
		this.x = x;
		this.y = y;
		this.z = z;
	}
	
	public double getZ() {
		return z;
	}
	
	public double getX() {
		return x;
	}
	
	public double getY() {
		return y;
	}
	
	public void setLocation(double x, double y, double z) {
		this.x = x;
		this.y = y;
		this.z = z;
	}
	
	@Override
	public String toString() {
		return "(" + this.x + ", " + this.y + ", " + this.z + ")";
	}
}
