package Model.Statements;

import Model.DataStructures.IDictionary;
import Model.DataStructures.IHeap;
import Model.Exceptions.EvaluationException;
import Model.Exceptions.ExecutionException;
import Model.Expressions.IExpression;
import Model.State.PrgState;
import Model.Types.IType;
import Model.Types.RefType;
import Model.Values.IValue;
import Model.Values.RefValue;

public class HeapWriteStatement implements IStatement {

    private final String varName;
    private final IExpression expression;


    public HeapWriteStatement(String varName, IExpression expression) {
        this.varName = varName;
        this.expression = expression;
    }

    @Override
    public PrgState execute(PrgState state) throws ExecutionException, EvaluationException {
        IDictionary<String, IValue> symTable = state.getSymTable();
        IHeap heap = state.getHeap();
        if (!symTable.containsKey(varName))
            throw new EvaluationException(varName + " is not present in the symbol table!");
        IValue varValue = symTable.get(varName);
        if (!(varValue instanceof RefValue referenceValue))
            throw new EvaluationException(varValue + " is not of type RefType!");
        IValue evaluated = expression.eval(symTable, heap);
        if (!evaluated.getType().equals(referenceValue.getLocationType()))
            throw new EvaluationException(evaluated + " is not of type " + referenceValue.getLocationType());
        heap.update(referenceValue.getAddr(), evaluated);
        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws EvaluationException {
        if (typeEnv.get(varName).equals(new RefType(expression.typeCheck(typeEnv))))
            return typeEnv;
        throw new EvaluationException("HeapWrite error: right hand side and left hand side have different types!");
    }


    @Override
    public String toString() {
        return "WriteHeap{" + varName + ", " + expression + "}";
    }
}
