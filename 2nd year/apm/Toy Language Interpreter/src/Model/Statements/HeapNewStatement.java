package Model.Statements;

import Model.Exceptions.EvaluationException;
import Model.Statements.IStatement;
import Model.Exceptions.ExecutionException;
import Model.State.PrgState;
import Model.DataStructures.IDictionary;
import Model.DataStructures.IHeap;
import Model.Expressions.IExpression;
import Model.Types.RefType;
import Model.Types.IType;
import Model.Values.RefValue;
import Model.Values.IValue;

public class HeapNewStatement implements IStatement {
    private final String variableName;
    private final IExpression expression;

    public HeapNewStatement(String varName, IExpression expression) {
        this.variableName = varName;
        this.expression = expression;
    }


    @Override
    public PrgState execute(PrgState state) throws ExecutionException, EvaluationException {
        IDictionary<String, IValue> symTable = state.getSymTable();
        IHeap heap = state.getHeap();
        // if the ref variable you are trying to give a new value to does not exist throw error
        if (!symTable.containsKey(variableName))
            throw new ExecutionException(variableName + " is not in the symbol table!");

        // if the variable you are trying to give a new value to is not of ref type throw error
        IValue varValue = symTable.get(variableName);
        if (!(varValue.getType() instanceof RefType))
            throw new EvaluationException(variableName + " is not of type RefType!");

        // evaluate the expression, find its location and check its type (it can be
        // a pointer of a pointer of int, for example)
        IValue evaluated = expression.eval(symTable, heap);
        IType locationType = ((RefValue) varValue).getLocationType();
        // if there is a type mismatch between the value you're giving and the variable, throw error
        if (!locationType.equals(evaluated.getType()))
            throw new EvaluationException(variableName+ " not of type "+ evaluated.getType()+"!");
        // find the first free position in the heap memory and add the variable
        Integer newPosition = heap.add(evaluated);
        symTable.put(variableName, new RefValue(newPosition, locationType)); // update symTable
        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws EvaluationException {
        IType typeVariable = typeEnv.get(variableName);
        IType typeExpression = expression.typeCheck(typeEnv);
        if (!typeVariable.equals(new RefType(typeExpression)))
            throw new EvaluationException("New error: right hand side and left hand side have different types!");
        return typeEnv;
    }

    @Override
    public String toString() {
        return "New{"+variableName+", "+expression+"}";
    }
}