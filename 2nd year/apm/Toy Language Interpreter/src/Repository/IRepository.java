package Repository;
import Model.Exceptions.ExecutionException;
import Model.State.PrgState;

import java.io.IOError;
import java.io.IOException;
import java.util.List;

public interface IRepository {
    PrgState getCurrentProgramState();
    void addProgramState(PrgState newProgramState);

    String getLogFilePath();

    void setProgramStates(List<PrgState> prgStates);

    List<PrgState> getProgramStates();

    void logProgramStateExecution(PrgState programState) throws IOException;
}
