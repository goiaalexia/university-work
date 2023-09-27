package Model.Statements;

import Model.DataStructures.IDictionary;
import Model.DataStructures.IHeap;
import Model.Exceptions.EvaluationException;
import Model.Exceptions.ExecutionException;
import Model.Expressions.IExpression;
import Model.State.PrgState;
import Model.Types.IType;
import Model.Values.IValue;

// v = 5
public class AssignStatement implements IStatement {
    public String id; // v
    public IExpression expression; // 5

    public AssignStatement(String id, IExpression expression) {
        this.id = id;
        this.expression = expression;
    }

    @Override
    public PrgState execute(PrgState state) throws ExecutionException, EvaluationException {
        IDictionary<String, IValue> symbolTable = state.getSymTable(); // variables
        IHeap hp = state.getHeap();
        IType type = symbolTable.get(id).getType(); // check type of declared variable
        IValue value = expression.eval(symbolTable, hp); // gets the value

        if (!value.getType().equals(type)) {
            throw new ExecutionException("Mismatch between variable type and assigned expression!");
        }
        if (!symbolTable.containsKey(id)) {
            throw new ExecutionException("Variable" + id + " was not declared in this scope!");
        }

        symbolTable.put(id, value); // assign

        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws EvaluationException {
        IType typeVar = typeEnv.get(id);
        IType typeExpression = expression.typeCheck(typeEnv);
        if (typeVar.equals(typeExpression))
            return typeEnv;
        else
            throw new EvaluationException("Assignment error: right hand side and left hand side have different types!");
    }

    @Override
    public String toString() {
        return id + "=" + expression;
    }

}
