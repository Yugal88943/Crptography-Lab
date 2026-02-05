import java.util.Scanner;

public class MatrixInverseSimple {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        double[][] a = new double[3][3];

        System.out.println("Enter elements of 3x3 matrix:");

        // Input
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                a[i][j] = sc.nextDouble();
            }
        }

        // Determinant
        double det =
                a[0][0] * (a[1][1]*a[2][2] - a[1][2]*a[2][1])
              - a[0][1] * (a[1][0]*a[2][2] - a[1][2]*a[2][0])
              + a[0][2] * (a[1][0]*a[2][1] - a[1][1]*a[2][0]);

        if (det == 0) {
            System.out.println("Matrix is singular. No inverse.");
            return;
        }

        // Adjoint matrix
        double[][] adj = new double[3][3];

        adj[0][0] =  (a[1][1]*a[2][2] - a[1][2]*a[2][1]);
        adj[0][1] = -(a[0][1]*a[2][2] - a[0][2]*a[2][1]);
        adj[0][2] =  (a[0][1]*a[1][2] - a[0][2]*a[1][1]);

        adj[1][0] = -(a[1][0]*a[2][2] - a[1][2]*a[2][0]);
        adj[1][1] =  (a[0][0]*a[2][2] - a[0][2]*a[2][0]);
        adj[1][2] = -(a[0][0]*a[1][2] - a[0][2]*a[1][0]);

        adj[2][0] =  (a[1][0]*a[2][1] - a[1][1]*a[2][0]);
        adj[2][1] = -(a[0][0]*a[2][1] - a[0][1]*a[2][0]);
        adj[2][2] =  (a[0][0]*a[1][1] - a[0][1]*a[1][0]);

        // Inverse = adjoint / determinant
        System.out.println("Inverse Matrix:");

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.printf("%6.2f ", adj[i][j] / det);
            }
            System.out.println();
        }

        sc.close();
    }
}
