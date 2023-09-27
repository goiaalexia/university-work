package Repository;

import Model.Exceptions.ExecutionException;
import Model.State.PrgState;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.LinkedList;
import java.util.List;

public class Repository implements IRepository{
    private List<PrgState> programStates;
    private final int currentPosition;
    private final String logFilePath;

    public Repository(String lfp) {
        programStates = new LinkedList<>();
        currentPosition = 0;
        logFilePath = lfp;
    }

    public String getLogFilePath() {
        return logFilePath;
    }

    @Override
    public void setProgramStates(List<PrgState> prgStates) {
        this.programStates = prgStates;
    }

    // DEPRECATED BECAUSE OF MULTITHREADING
    @Override
    public PrgState getCurrentProgramState() {
        return programStates.get(currentPosition);
    }

    @Override
    public List<PrgState> getProgramStates() {
        return programStates;
    }

    @Override
    public void addProgramState(PrgState newProgramState) {
        programStates.add(newProgramState);
    }

    @Override
    public String toString(){
        return this.getCurrentProgramState().toString();
    }

    @Override
    public void logProgramStateExecution(PrgState programState) throws IOException {
        PrintWriter logFile;
        logFile = new PrintWriter(new BufferedWriter(new FileWriter(logFilePath, true)));
        logFile.println(programState.toString());
        logFile.close();
    }
}