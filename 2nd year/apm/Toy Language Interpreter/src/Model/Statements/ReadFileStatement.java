package Model.Statements;

import Model.DataStructures.IDictionary;
import Model.DataStructures.IHeap;
import Model.Exceptions.EvaluationException;
import Model.Exceptions.ExecutionException;
import Model.Expressions.IExpression;
import Model.State.PrgState;
import Model.Types.IType;
import Model.Types.IntType;
import Model.Types.StringType;
import Model.Values.IValue;
import Model.Values.IntValue;
import Model.Values.StringValue;

import java.io.BufferedReader;
import java.io.IOException;

public class ReadFileStatement implements IStatement {

    private final IExpression expression;
    private final String varName;

    public ReadFileStatement(IExpression expression, String varName) {
        this.expression = expression;
        this.varName = varName;
    }

    @Override
    public PrgState execute(PrgState state) throws ExecutionException, EvaluationException {
        IDictionary<String, IValue> symTable = state.getSymTable();
        IHeap hp = state.getHeap();
        IDictionary<StringValue, BufferedReader> fileTable = state.getFileTable();
        if (!symTable.containsKey(varName))
            throw new EvaluationException(varName + " is not present in the symTable!");

        IValue value = symTable.get(varName);

        if (!value.getType().equals(new IntType()))
            throw new EvaluationException(value + " is not of type IntType!");
        value = expression.eval(symTable, hp);
        if (!value.getType().equals(new StringType()))
            throw new EvaluationException(value + " does not evaluate to StringType!");
        StringValue castValue = (StringValue) value;
        if (!fileTable.containsKey(castValue))
            throw new EvaluationException("the fileTable does not contain " + castValue.getStrval() + "!");
        BufferedReader br = fileTable.get(castValue);
        try {
            String line = br.readLine();
            if (line == null)
                line = "0";
            symTable.put(varName, new IntValue(Integer.parseInt(line)));
        } catch (IOException e) {
            throw new EvaluationException("could not read from file" + castValue.getStrval() + "!");
        }
        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws EvaluationException {
        if (!expression.typeCheck(typeEnv).equals(new StringType()))
            throw new EvaluationException("ReadFile requires a StringType as variable parameter!");
        if (!typeEnv.get(varName).equals(new IntType()))
            throw new EvaluationException("ReadFile requires an IntType as variable parameter!");
        return typeEnv;
    }

    @Override
    public String toString() {
        return "ReadFile{" + expression + ", " + varName + "}";
    }
}
