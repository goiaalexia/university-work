package view;


import controller.Service;
import model.Eggplant;
import model.Pepper;
import model.Tomato;
import model.Vegetable;
import repository.Repo;
import repository.RepoException;

import java.util.Scanner;

public class UserInterface {

    private Service serv;

    public UserInterface(Repo r) {
        this.serv = new Service(r);
    }

    public UserInterface(){
        this.serv = new Service();
    }

    public void printMenu() {
        System.out.println("MAIN MENU\n1 - Display all vegetables.\n2 - Add new vegetable.\n3 - Remove vegetable.\n4 - Display vegetables > 0.2 kg.\n5 - Exit.\n\nOption: ");
    }

    public int getOption() {
        Scanner console = new Scanner(System.in);
        return console.nextInt();
    }

    public void run() {
        while (true) {
            int opt;
            printMenu();
            opt = getOption();
            switch (opt) {
                case 1 -> {
                    for(int i=0; i<this.serv.getElements().getFill(); i++)
                        System.out.println(this.serv.getElements().getElement(i).toString());
                }
                case 2 -> {
                    Vegetable v;
                    String type;
                    float weight;
                    Scanner console = new Scanner(System.in);
                    System.out.println("Type: ");
                    type = console.nextLine();
                    System.out.println("Weight: ");
                    weight = console.nextFloat();
                    switch (type){
                        case "eggplant" -> v = new Eggplant(weight);
                        case "tomato" -> v = new Tomato(weight);
                        case "pepper" -> v = new Pepper(weight);
                        default -> {
                            System.out.println("Not a valid vegetable!");
                            continue;
                        }
                    }
                    this.serv.addVegetable(v);
                }
                case 3 -> {
                    System.out.println("Index of vegetable to be removed: ");
                    Scanner console = new Scanner(System.in);
                    int index = console.nextInt();
                    try {
                        this.serv.removeVegetable(index);
                    }
                    catch (RepoException r){
                        System.out.println(r.getMessage());
                    }
                }
                case 4 -> {
                    int sizeOfRepo = this.serv.weightedVegetables().getFill();
                    for(int i=0; i< sizeOfRepo; i++)
                        System.out.println(this.serv.weightedVegetables().getElement(i).toString()+"\n");
                }
                case 5 -> {
                    System.out.println("Goodbye!");
                    return;
                }
                default -> System.out.println("Invalid option!");
            }
        }

    }

}
