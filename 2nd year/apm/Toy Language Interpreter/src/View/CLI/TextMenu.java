package View.CLI;

import View.Commands.Command;

public class TextMenu {
    private final java.util.Map<String, Command> commands;

    public TextMenu() {
        this.commands = new java.util.HashMap<>();
    }

    public void addCommand(Command c) {
        this.commands.put(c.getKey(), c);
    }

    private void printMenu() {
        for(Command c : this.commands.values()) {
            String line = String.format("%4s : %s", c.getKey(), c.getDescription());
            System.out.println(line);
        }
    }

    @SuppressWarnings("InfiniteLoopStatement")
    public void show() {
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        while(true) {
            printMenu();
            System.out.println("Input option: ");
            String key = scanner.nextLine();
            Command c = this.commands.get(key);
            if(c == null) {
                System.out.println("Invalid option!");
                continue;
            }
            c.execute();
        }
    }
}