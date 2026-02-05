import java.util.Scanner;

public class Matrix_Multiplication {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the number of rows for the first matrix (A):");
        int rowsA = scanner.nextInt();
        System.out.println("Enter the number of columns for the first matrix (A):");
        int colsA = scanner.nextInt();

        System.out.println("Enter the number of rows for the second matrix (B):");
        int rowsB = scanner.nextInt();
        System.out.println("Enter the number of columns for the second matrix (B):");
        int colsB = scanner.nextInt();

        if (colsA != rowsB) {
            System.out.println("\nError: Matrix multiplication is not possible.");
            System.out.println("The number of columns in the first matrix must equal the number of rows in the second matrix.");
            return; 
        }

        int[][] matrixA = new int[rowsA][colsA];
        int[][] matrixB = new int[rowsB][colsB];
        int[][] resultMatrix = new int[rowsA][colsB];

        System.out.println("\nEnter elements of the first matrix (A):");
        for (int i = 0; i < rowsA; i++) {
            for (int j = 0; j < colsA; j++) {
                System.out.print("A[" + i + "][" + j + "]: ");
                matrixA[i][j] = scanner.nextInt();
            }
        }

        System.out.println("\nEnter elements of the second matrix (B):");
        for (int i = 0; i < rowsB; i++) {
            for (int j = 0; j < colsB; j++) {
                System.out.print("B[" + i + "][" + j + "]: ");
                matrixB[i][j] = scanner.nextInt();
            }
        }
  
        for (int i = 0; i < rowsA; i++) {
            for (int j = 0; j < colsB; j++) {
                for (int k = 0; k < colsA; k++) {
                    resultMatrix[i][j] += matrixA[i][k] * matrixB[k][j];
                }
            }
        }

        System.out.println("\nResultant Matrix:");
        for (int i = 0; i < rowsA; i++) {
            for (int j = 0; j < colsB; j++) {
                System.out.print(resultMatrix[i][j] + " ");
            }
            System.out.println(); 
        }

        scanner.close(); 
    }
}