package Model.Statements;

import Model.DataStructures.IDictionary;
import Model.Exceptions.EvaluationException;
import Model.Exceptions.ExecutionException;
import Model.Expressions.IExpression;
import Model.State.PrgState;
import Model.Types.IType;
import Model.Types.StringType;
import Model.Values.IValue;
import Model.Values.StringValue;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class OpenReadFileStatement implements IStatement {

    private final IExpression exp;

    public OpenReadFileStatement(IExpression exp) {
        this.exp = exp;
    }

    @Override
    public PrgState execute(PrgState state) throws ExecutionException, EvaluationException {
        IValue value = exp.eval(state.getSymTable(), state.getHeap());
        if (!value.getType().equals(new StringType()))
            throw new EvaluationException(exp+" does not evaluate to StringType!");
        StringValue fileName = (StringValue) value;
        IDictionary<StringValue, BufferedReader> fileTable = state.getFileTable();
        if (fileTable.containsKey(fileName))
            throw new ExecutionException(fileName+" is already opened!");
        BufferedReader br;
        try {
            br = new BufferedReader(new FileReader(fileName.getStrval()));
        } catch (IOException e) {
            throw new EvaluationException(fileName+" could not be opened!");
        }
        fileTable.put(fileName, br);
        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws EvaluationException {
        if (!exp.typeCheck(typeEnv).equals(new StringType()))
            throw new EvaluationException("OpenReadFile error: StringType expression required!");
        return typeEnv;
    }

    @Override
    public String toString() {
        return "OpenReadFile{"+exp+"}";
    }
}
