
//package FirstFit;
import java.util.Scanner;

public class Memory_placement {
    static int job[];
    static int block[];
    static int js, bs;
    static Scanner input = new Scanner(System.in);
    static int Allocation[];

    public static void main(String args[]) {
        Memory_placement MA = new Memory_placement();

        System.out.println("\nEnter total no. of jobs:");
        js = Integer.parseInt(input.nextLine());

        System.out.println("\nEnter total no. of blocks:");
        bs = Integer.parseInt(input.nextLine());

        job = new int[js];
        block = new int[bs];

        MA.ReadData(js, bs);
        MA.Firstfit();
        MA.NextFit();
        MA.BestFit();
        MA.WorstFit();

        
    }

    void ReadData(int n, int m) {
        for (int i = 0; i < n; i++) {
            System.out.println("Enter Job Size:");
            job[i] = Integer.parseInt(input.nextLine());
        }
        for (int i = 0; i < m; i++) {
            System.out.println("Enter Block Size:");
            block[i] = Integer.parseInt(input.nextLine());
        }
    }

    void Firstfit() {
        int flag = 0;
        Allocation = new int[js];
        for (int i = 0; i < Allocation.length; i++) {
            Allocation[i] = -1;
        }
        for (int i = 0; i < js; i++) {
            for (int j = 0; j < bs; j++) {
                flag = 0;
                if (block[j] >= job[i]) {
                    for (int k = 0; k < js; k++) {
                        if (Allocation[k] == j)
                            flag = 1;
                    }
                    if (flag == 0) {
                        Allocation[i] = j;
                        break;
                    }
                }
            }
        }
        System.out.println("\nFIRST FIT: \n");
        Display();
    }

    void Display() {
        System.out.println("\tJob No.\tJob Size\tBlock No.\tFragment");
        for (int i = 0; i < js; i++) {
            System.out.print("\t" + (i + 1) + "\t\t" + job[i] + "\t\t");
            if (Allocation[i] != -1) {
                System.out.println(Allocation[i] + "\t\t" + (block[Allocation[i]] - job[i]));
            } else {
                System.out.println("Not Allocated");
            }
        }
    }

    void BestFit() {
        int flag = 0;
        Allocation = new int[js];
        for (int i = 0; i < Allocation.length; i++) {
            Allocation[i] = -1;
        }
        for (int i = 0; i < js; i++) {
            int BestInd = -1;
            for (int j = 0; j < bs; j++) {
                flag = 0;
                if (block[j] >= job[i]) {
                    for (int k = 0; k < js; k++) {
                        if (Allocation[k] == j) {
                            flag = 1;
                            break;
                        }
                    }
                    if (BestInd == -1 && flag == 0) {
                        BestInd = j;
                    } else if (flag == 0 && block[BestInd] > block[j]) {
                        BestInd = j;
                    } else {
                        continue;
                    }
                }
            }
            if (BestInd != -1) {
                Allocation[i] = BestInd;
            }
        }
         System.out.println("\nBEST FIT: \n");
        Display();
    }

    void WorstFit() {
        Allocation = new int[js];
        for (int i = 0; i < Allocation.length; i++) {
            Allocation[i] = -1;
        }
        for (int i = 0; i < js; i++) {
            int worstBlockIndex = -1;
            for (int j = 0; j < bs; j++) {
                if (block[j] >= job[i]) {
                    if (worstBlockIndex == -1 || block[j] > block[worstBlockIndex]) {
                        worstBlockIndex = j;
                    }
                }
            }
            if (worstBlockIndex != -1) {
                Allocation[i] = worstBlockIndex;
                block[worstBlockIndex] -= job[i];
            }
        }
         System.out.println("\nWORST FIT: \n");
        Display();
    }

    void NextFit() {
        int flag = 0;
        Allocation = new int[js];
        for (int i = 0; i < Allocation.length; i++) {
            Allocation[i] = -1;
        }
        int lastAllocatedBlockIndex = -1;
        for (int i = 0; i < js; i++) {
            for (int j = lastAllocatedBlockIndex + 1; j < bs; j++) {
                flag = 0;
                if (block[j] >= job[i]) {
                    lastAllocatedBlockIndex = j;
                    for (int k = 0; k < js; k++) {
                        if (Allocation[k] == j) {
                            flag = 1;
                            break;
                        }
                    }
                    if (flag == 0) {
                        Allocation[i] = j;
                        break;
                    }
                }
            }
        }
         System.out.println("\nNEXT FIT: \n");
        Display();
    }
}
