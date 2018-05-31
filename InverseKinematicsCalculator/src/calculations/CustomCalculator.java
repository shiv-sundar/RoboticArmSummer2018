package calculations;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Random;
import java.util.Scanner;

public class CustomCalculator {
	private double[] armDistances;
	public double totalLength;

	public CustomCalculator(double[] armDistances) {
		this.armDistances = armDistances;
		totalLength = 0;
		for (int x = 0; x < armDistances.length; x++) {
			totalLength += armDistances[x];
		}
	}

	public double[] calculateArmAngles(Point3D endPoint) {
		double[] angles = new double[3];
		if (!canReach(endPoint)) {
			System.out.println("That is not a possible destination.");
			throw new IllegalArgumentException();
		}

		else if (endPoint.getX() == totalLength) {
			angles[0] = 0;
			angles[1] = 0;
			angles[2] = 0;
		}

		else if (endPoint.getX() == totalLength * -1) {
			angles[0] = 180;
			angles[1] = 0;
			angles[2] = 0;
		}

		else if (endPoint.getY() == totalLength) {
			angles[0] = 0;
			angles[1] = 90;
			angles[2] = 180;
		}

		else if (endPoint.getZ() == totalLength) {
			angles[0] = 90;
			angles[1] = 0;
			angles[2] = 180;
		}

		else if (endPoint.getZ() == totalLength * -1) {
			angles[0] = 270;
			angles[1] = 0;
			angles[2] = 180;
		}

		else {
			if (endPoint.getZ() >= 0) {
				angles[0] = Math.toDegrees(Math.atan2(endPoint.getZ(), endPoint.getX()));
			}

			else {
				angles[0] = 360 + Math.toDegrees(Math.atan2(endPoint.getZ(), endPoint.getX()));
			}

			double newDist = distance(0, 0, 0, endPoint.getX(), 0, endPoint.getZ());
			double value = (Math.pow(newDist, 2) + Math.pow(endPoint.getY(), 2) - Math.pow(armDistances[1], 2) - Math.pow(armDistances[0], 2))/(2*armDistances[0]*armDistances[1]);
			angles[2] = Math.toDegrees(Math.atan2(Math.sqrt(1 - value), value));
			angles[1] = 90 - Math.toDegrees(Math.atan2(newDist, endPoint.getX()) + Math.atan2(armDistances[1] * Math.sin(angles[2]), armDistances[0] + (armDistances[1] * Math.cos(angles[2]))));
		}

		return angles;
	}

	private double distance(double ox, double oy, double oz, double ex, double ey, double ez) {
		return Math.sqrt(Math.pow(ex - ox, 2) + Math.pow(ey - oy, 2) + Math.pow(ez - oz, 2));
	}

	public boolean canReach(Point3D point) {
		return distance(0, 0, 0, point.getX(), point.getY(), point.getZ()) <= totalLength;
	}

	public Point3D[] generateRandPoints(int numPoints) {
		Point3D[] randPoints = new Point3D[numPoints];
		Random rand = new Random(7);
		for (int i = 0; i < numPoints; i++) {
			double dist = totalLength * rand.nextDouble();
			double angleXZ = 2 * Math.PI * rand.nextDouble();
			double angleXZY = .5 * Math.PI * rand.nextDouble();
			double distXZ = dist * Math.cos(angleXZY);
			double distY = Math.abs(dist * Math.sin(angleXZY));
			double distX = distXZ * Math.cos(angleXZ);
			double distZ = distXZ * Math.sin(angleXZ);
			randPoints[i] = new Point3D(distX, distY, distZ);
		}

		return randPoints;
	}

	public void printNewNetworkPts(int numPoints) {
		Point3D[] randPts = generateRandPoints(numPoints);
		double[][] randAngles = new double[numPoints][3];
		for (int i = 0; i < randPts.length; i++) {
			double[] newValues = calculateArmAngles(randPts[i]);
			for (int j = 0; j < newValues.length; j++) {
				randAngles[i][j] = newValues[j];
			}
		}

		System.out.println("Inputs: ");
		System.out.print("([");
		for (int i = 0; i < randPts.length; i++) {
			if (i == randPts.length - 1) {
				System.out.print("[" + ((randPts[i].getZ())) + ", " + ((randPts[i].getX())) + "]");
			}

			else {
				System.out.println("[" + ((randPts[i].getZ())) + ", " + ((randPts[i].getX())) + "], ");
			}

			//			System.out.print(randPts[i].getZ()/randPts[i].getX() + " ");
		}

		System.out.println("])");
		System.out.println("Outputs: ");
		System.out.print("([");
		for (int i = 0; i < randPts.length; i++) {
			if (i == randPts.length - 1) {
				System.out.print("[" + randAngles[i][0]/360 + "]");
			}

			else {
				System.out.println("[" + randAngles[i][0]/360 + "], ");
			}

			//			System.out.print(randAngles[i][0] + " ");
		}

		System.out.println("])");
	}

	public static void main(String[] args) throws FileNotFoundException {
		double[] armDist = new double[2];
		Scanner scan = new Scanner(System.in);
		System.out.println("Length of arm 1");
		armDist[0] = scan.nextDouble();
		System.out.println("Length of arm 2");
		armDist[1] = scan.nextDouble();
		File file = new File("Inputs.txt");
		PrintWriter pw = new PrintWriter(file);
		File fileOutput = new File("Outputs.txt");
		PrintWriter pw1 = new PrintWriter(fileOutput);
		CustomCalculator calc = new CustomCalculator(armDist);
		//		System.out.println("What is the x value of the target point?: ");
		//		double x = scan.nextDouble();
		//		System.out.println("What is the y value of the target point?: ");
		//		double y = scan.nextDouble();
		//		System.out.println("What is the z value of the target point?: ");
		//		double z = scan.nextDouble();
		//		Point3D endPoint = new Point3D(x, y, z);
		//		double[] angles = calc.calculateArmAngles(endPoint);
		//		System.out.println("Servo 0 AoR = " + angles[0]);
		//		System.out.println("Servo 1 AoR = " + angles[1]);
		//		System.out.println("Servo 2 AoR = " + angles[2]);
		System.out.println("How many data points would you like to generate?: ");
		int numPoints = scan.nextInt();
		//		calc.printNewNetworkPts(numPoints);
		if (numPoints != 1) {
			double[] test = new double[numPoints];
			double[] angles = new double[numPoints];
			double step = 200.0/numPoints;
			for (int x = 0; x < numPoints; x++) {
				test[x] = -100 + (step * x);
				angles[x] = Math.atan(test[x]);
			}
//			Point3D[] randPts = calc.generateRandPoints(numPoints);
//			double[][] randAngles = new double[numPoints][3];
//			for (int i = 0; i < randPts.length; i++) {
//				double[] newValues = calc.calculateArmAngles(randPts[i]);
//				for (int j = 0; j < newValues.length; j++) {
//					randAngles[i][j] = newValues[j];
//				}
//			}
//
//			pw.print("([");
//			for (int i = 0; i < randPts.length; i++) {
//				if (i == randPts.length - 1) {
//					pw.print("[" + (randPts[i].getZ())/(randPts[i].getX()) + "]");
//					//							"[" + (randPts[i].getX() + calc.totalLength)/(calc.totalLength*2) + ", " + (randPts[i].getY() + calc.totalLength)/(calc.totalLength*2) + ", " + (randPts[i].getZ() + calc.totalLength)/(calc.totalLength*2) + "]");
//				}
//
//				else {
//					pw.println("[" + ((randPts[i].getZ()))/((randPts[i].getX())) + "], ");
//					//							"[" + (randPts[i].getX() + calc.totalLength)/(calc.totalLength*2) + ", " + (randPts[i].getY() + calc.totalLength)/(calc.totalLength*2) + ", " + (randPts[i].getZ() + calc.totalLength)/(calc.totalLength*2) + "], ");
//				}
//			}
//
//			pw.println("])");
//			pw1.print("([");
//			for (int i = 0; i < randPts.length; i++) {
//				if (i == randPts.length - 1) {
//					pw1.print("[" + randAngles[i][0]/360 + "]");
//					//							"[" + randAngles[i][0]/360 + ", " + (randAngles[i][1] + 360)/720 + ", " + randAngles[i][2]/180 + "]");
//				}
//
//				else {
//					pw1.println("[" + randAngles[i][0]/360 + "], ");
//					//							"[" + randAngles[i][0]/360 + ", " + (randAngles[i][1] + 360)/720 + ", " + randAngles[i][2]/180 + "], ");
//				}
//			}
//
//			pw1.println("])");
			pw.print("([");
			for (int i = 0; i < test.length; i++) {
				if (i == test.length - 1) {
					pw.print("[" + (test[i]) + "]");
					//							"[" + (randPts[i].getX() + calc.totalLength)/(calc.totalLength*2) + ", " + (randPts[i].getY() + calc.totalLength)/(calc.totalLength*2) + ", " + (randPts[i].getZ() + calc.totalLength)/(calc.totalLength*2) + "]");
				}

				else {
					pw.println("[" + (test[i]) + "], ");
					//							"[" + (randPts[i].getX() + calc.totalLength)/(calc.totalLength*2) + ", " + (randPts[i].getY() + calc.totalLength)/(calc.totalLength*2) + ", " + (randPts[i].getZ() + calc.totalLength)/(calc.totalLength*2) + "], ");
				}
			}
			
			pw.println("])");
			pw1.print("([");
			for (int i = 0; i < angles.length; i++) {
				if (i == angles.length - 1) {
					pw1.print("[" + angles[i] + "]");
					//							"[" + randAngles[i][0]/360 + ", " + (randAngles[i][1] + 360)/720 + ", " + randAngles[i][2]/180 + "]");
				}

				else {
					pw1.println("[" + angles[i] + "], ");
					//							"[" + randAngles[i][0]/360 + ", " + (randAngles[i][1] + 360)/720 + ", " + randAngles[i][2]/180 + "], ");
				}
			}
			
			pw1.println("])");
			System.out.println("Data points generated");
		}

		else {
			Point3D[] randPts = calc.generateRandPoints(numPoints);
			double[][] randAngles = new double[numPoints][3];
			for (int i = 0; i < randPts.length; i++) {
				double[] newValues = calc.calculateArmAngles(randPts[i]);
				for (int j = 0; j < newValues.length; j++) {
					randAngles[i][j] = newValues[j];
				}
			}

			System.out.println("Inputs: ");
			System.out.println("([[" + (randPts[0].getZ())/(randPts[0].getX()) + "]])");
			System.out.println("Outputs: ");
			System.out.println("([[" + randAngles[0][0]/360 + "]])");
		}
		//		calc.printNewNetworkPts(numPoints);

		pw.close();
		pw1.close();
		scan.close();
	}
}