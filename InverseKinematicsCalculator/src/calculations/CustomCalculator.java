package calculations;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.ArrayList;
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

		else if (endPoint.getX() == -totalLength) {
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

		else if (endPoint.getZ() == -totalLength) {
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
		Point3D[] randPoints = new Point3D[numPoints + 5];
		Random rand = new Random();
		int i;
		for (i = 0; i < numPoints; i++) {
			double dist = totalLength * rand.nextDouble();
			double angleXZ = 2 * Math.PI * rand.nextDouble();
			double angleXZY = .5 * Math.PI * rand.nextDouble();
			double distXZ = dist * Math.cos(angleXZY);
			double distY = Math.abs(dist * Math.sin(angleXZY));
			double distX = distXZ * Math.cos(angleXZ);
			double distZ = distXZ * Math.sin(angleXZ);
			randPoints[i] = new Point3D(distX, distY, distZ);
		}

		randPoints[numPoints] = new Point3D(totalLength, 0, 0);
		randPoints[numPoints + 1] = new Point3D(-totalLength, 0, 0);
		randPoints[numPoints + 2] = new Point3D(0, totalLength, 0);
		randPoints[numPoints + 3] = new Point3D(0, 0, totalLength);
		randPoints[numPoints + 4] = new Point3D(0, 0, -totalLength);
		return randPoints;
	}

	public Point3D[] generateDataPoints(int split, int numDist) {
		double numXZAng = (2 * Math.PI)/split;
		double numXZYAng = (.5 * Math.PI)/split;
		Point3D[] dataPoints = new Point3D[(int) numDist * split * split];
		int whichPt = 0;
		for (int i = 0; i < split; i++) {
			for (int j = 0; j < split; j++) {
				for (double dist = totalLength - .005; dist > 0; dist -= totalLength/numDist) {
					double angleXZY = 0 + (numXZYAng * i);
					double angleXZ = 0 + (numXZAng * j);
					double distXZ = dist * Math.cos(angleXZY);
					double distY = Math.abs(dist * Math.sin(angleXZY));
					double distX = distXZ * Math.cos(angleXZ);
					double distZ = distXZ * Math.sin(angleXZ);
					Point3D newPoint = new Point3D(distX, distY, distZ);
					dataPoints[whichPt] = newPoint;
					whichPt++;
				}
			}
		}

		return dataPoints;
	}

	public static void main(String[] args) throws FileNotFoundException {
		Scanner scan = new Scanner(System.in);
		System.out.println("Which language is this array for? (\"a\" for Arduino, \"p\" for Python):");
		String lang = scan.next();
		if (lang.toCharArray()[0] == 'a' || lang.toCharArray()[0] == 'A') {
			File arduinoIn = new File("ardInput.txt");
			PrintWriter pwIn = new PrintWriter(arduinoIn);
			ArrayList<Double> ALD = new ArrayList<Double>();
			ArrayList<double[]> ALALD = new ArrayList<double[]>();
			System.out.println("Copy the Python array:");
			scan.useDelimiter("\r\n|[\r\n]"); 
			String pyArray = scan.next();
			for (int x = 0; x < 2; x++) {
				pyArray += scan.nextLine();
				pyArray += "\n";
			}

			Scanner scan1 = new Scanner(pyArray);
			Scanner scan2 = null;
			while (scan1.hasNextLine()) {
				scan2 = new Scanner(scan1.nextLine());
				while (scan2.hasNextDouble()) {
					ALD.add(scan2.nextDouble());
				}

				double[] vals = new double[ALD.size()];
				for (int x = 0; x < ALD.size(); x++) {
					vals[x] = ALD.get(x);
				}

				ALALD.add(vals);
				ALD.removeAll(ALD);
			}

			double[][] testArray = new double[ALALD.size()][ALALD.get(0).length];
			for (int x = 0; x < testArray.length; x++) {
				for (int y = 0; y < testArray[0].length; y++) {
					testArray[x][y] = ALALD.get(x)[y];
				}
			}

			pwIn.println("double syn0[2][50] = {");
			for (int x = 0; x < testArray.length; x++) {
				pwIn.print("{");
				for (int y = 0; y < testArray[0].length; y++) {
					if (y == testArray[0].length - 1) {
						pwIn.print(testArray[x][y]);
					}

					else {
						pwIn.print(testArray[x][y] + ", ");
					}
				}

				if (x == testArray.length - 1) {
					pwIn.println("}");
				}

				else {
					pwIn.println("},");
				}
			}

			pwIn.println("};");
			pwIn.close();
			scan1.close();
			scan2.close();
		}

		else if (lang.toCharArray()[0] == 'p' || lang.toCharArray()[0] == 'P') {
			double[] armDist = new double[2];
			System.out.println("Length of arm 1");
			armDist[0] = scan.nextDouble();
			System.out.println("Length of arm 2");
			armDist[1] = scan.nextDouble();
			CustomCalculator calc = new CustomCalculator(armDist);
			File pythonIn = new File("PythonInput.txt");
			PrintWriter pwIn = new PrintWriter(pythonIn);
			File pythonOut = new File("PythonOutput.txt");
			PrintWriter pwOut = new PrintWriter(pythonOut);
			System.out.println("Split for angles: ");
			int numPoints = scan.nextInt();
			if (numPoints != 0) {
				System.out.println("Split for distance: ");
				int numDist = scan.nextInt();
				Point3D[] newPts = calc.generateDataPoints(numPoints, numDist);
				double[][] randAngles = new double[newPts.length][3];
				for (int i = 0; i < newPts.length; i++) {
					double[] newValues = calc.calculateArmAngles(newPts[i]);
					for (int j = 0; j < newValues.length; j++) {
						randAngles[i][j] = newValues[j];
					}
				}

				pwIn.print("([");
				for (int i = 0; i < newPts.length; i++) {
					if (i == newPts.length - 1) {
						pwIn.print("[" + (newPts[i].getZ()) + ", " + (newPts[i].getX()) + "]");
					}

					else {
						pwIn.println("[" + ((newPts[i].getZ())) + ", " + (newPts[i].getX()) + "], ");
					}
				}

				pwIn.println("])");
				pwOut.print("([");
				for (int i = 0; i < newPts.length; i++) {
					if (i == newPts.length - 1) {
						pwOut.print("[" + randAngles[i][0]/360 + "]");
					}

					else {
						pwOut.println("[" + randAngles[i][0]/360 + "], ");
					}
				}

				pwOut.println("])");
				System.out.println("Data points generated");
			}

			else {
				Point3D[] randPts = calc.generateRandPoints(1);
				double[][] randAngles = new double[1][3];
				double[] newValues = calc.calculateArmAngles(randPts[0]);
				for (int j = 0; j < newValues.length; j++) {
					randAngles[0][j] = newValues[j];
				}

				System.out.println("Inputs: ");
				System.out.println("([[" + (randPts[0].getZ()) + ", " + (randPts[0].getX()) + "]])");
				System.out.println("Outputs: ");
				System.out.println("([[" + randAngles[0][0]/360 + "]])");
			}

			pwOut.close();
			pwIn.close();
		}

		else {
			System.out.println("That is not a valid option");
		}

		scan.close();
	}
}