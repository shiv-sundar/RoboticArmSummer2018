package calculations;

import java.awt.geom.Point2D;
import java.util.ArrayList;
import java.util.Scanner;

public class Calculator {
	private double[] angles;
	private double[] armDistances;

	public Calculator(double[] armDistances) {
		this.armDistances = armDistances;
	}

	public double[] calculateArmAngles(Point2D.Double endPoint) {
		System.out.println("Angles given are relative to previous arm, beginning from the origin");
		angles = new double[armDistances.length];
		double totalLength = 0;
		for (int x = 0; x < armDistances.length; x++) {
			totalLength += armDistances[x];
		}

		double totalDistance = distance(new Point2D.Double(), endPoint);
		if (totalDistance > totalLength) {
			System.out.println("That is not a possible destination.");
		}

		else if (totalDistance == totalLength) {
			for (int x = 0; x < angles.length; x++) {
				if (x == 0) {
					angles[x] = calculateAngleFromPoints(new Point2D.Double(), endPoint);
				}

				else {
					angles[x] = 180;
				}
			}
		}

		else {
			for (int x = armDistances.length - 1; x >= 0; x--) {
				double slope = calculateSlope(new Point2D.Double(), endPoint);
				//need to fix this, have to figure out some way to get the best point
				double distance = armDistances[x];
				Point2D.Double point1 = calculatePointFromSlope(endPoint, slope, distance);
				angles[x] = calculateAngleFromPoints(point1, endPoint);
				endPoint = point1;
			}

			//need to start calculating the shortest distance
		}
		
//		for (int x = 0; x < angles.length; x++) {
//			System.out.println(angles[x]);
//		}
		
		return angles;
	}

	private double calculateSlope(Point2D.Double origin, Point2D.Double end) {
		if (end.getX() == origin.getX()) {
			if (end.getY() > origin.getY()) {
				return Double.POSITIVE_INFINITY;
			}

			else {
				return Double.NEGATIVE_INFINITY;
			}
		}

		return (end.getY() - origin.getY())/(end.getX() - origin.getX());
	}

	private Point2D.Double calculatePointFromSlope(Point2D.Double end, double slope, double distance) {
		Point2D.Double returnPoint = new Point2D.Double();
		if (slope == Double.POSITIVE_INFINITY) {
			returnPoint.setLocation(end.getX(), end.getY() + distance);
			return returnPoint;
		}

		else if (slope == Double.NEGATIVE_INFINITY) {
			returnPoint.setLocation(end.getX(), end.getY() - distance);
			return returnPoint;
		}

		double dx = (distance/Math.sqrt(1 + (slope * slope)));
		double dy = slope*dx;
		returnPoint.setLocation(end.getX() - dx, end.getY() - dy);
		return returnPoint;
	}
	
	private double distance(Point2D.Double origin, Point2D.Double end) {
		return Math.sqrt(Math.pow((end.getX() - origin.getX()), 2) + Math.pow((end.getY() - origin.getY()), 2));
	}
	
	private double calculateAngleFromPoints(Point2D.Double origin, Point2D.Double endPoint) {
		return Math.toDegrees(Math.atan2((endPoint.getY() - origin.getY()), (endPoint.getX() - origin.getX())));
	}

	public static void main(String[] args) {
		int numJoints;
		Scanner scan = new Scanner(System.in);
		do {
			System.out.println("Number of joints: ");
			numJoints = scan.nextInt();
		} while (numJoints <= 0);

		ArrayList<Double> ali = new ArrayList<Double>();
		System.out.println("The next step must list joint distances from the origin outwards to the tooltip.");
		for (int x = 1; x <= numJoints; x++) {
			if (x != numJoints) {
				System.out.println("Distance from servo " + x + " to servo " + (x + 1) + ": ");
				ali.add(scan.nextDouble());
			}
			
			else if (x == numJoints) {
				System.out.println("Distance from servo " + x + " to end effector: ");
				ali.add(scan.nextDouble());
			}
		}

		double[] armDistances = new double[ali.size()];
		for (int x = 0; x < armDistances.length; x++) {
			armDistances[x] = ali.get(x);
		}

		Calculator calc = new Calculator(armDistances);
		System.out.println("What is the x value of the target point?: ");
		double x = scan.nextDouble();
		System.out.println("What is the y value of the target point?: ");
		double y = scan.nextDouble();
		Point2D.Double endPoint = new Point2D.Double(x, y);
		calc.calculateArmAngles(endPoint);
		scan.close();
	}
}