package Model.Statements;

import Model.DataStructures.IDictionary;
import Model.Exceptions.EvaluationException;
import Model.Exceptions.ExecutionException;
import Model.State.PrgState;
import Model.Types.IType;

public interface IStatement {
    PrgState execute(PrgState state) throws ExecutionException, EvaluationException;       //which is the execution method for a statement

    IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws EvaluationException;

}
