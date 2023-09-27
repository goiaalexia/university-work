package View.Commands;

import Controller.Controller;
import Model.Statements.IStatement;

public class RunCommand extends Command {
    private final Controller controller;
    IStatement command;

    public RunCommand(IStatement s1, String key, String description, Controller controller) {
        super(key, description);
        this.controller = controller;
        this.command = s1;
    }

    @Override
    public void execute() {
        try {
            // so that we can rerun each example without having the previous output and nothing left to run.
            Controller copy = new Controller(controller.logFilePath, controller.stepByStep, command);
            if (copy.stepByStep) {
                copy.stepByStepExecution();
            } else {
                copy.allStep();
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        System.out.println("Result: " + controller.getRepository().getCurrentProgramState().outToString());
    }
}