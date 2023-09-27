package Model.Statements;

import Model.DataStructures.IDictionary;
import Model.Exceptions.EvaluationException;
import Model.State.PrgState;
import Model.Types.IType;
import Model.Values.IValue;

// int v;
public class VarDeclarationStatement implements IStatement {
    public String name;
    public IType type;

    public VarDeclarationStatement(String name, IType type) {
        this.name = name;
        this.type = type;
    }

    @Override
    public PrgState execute(PrgState state) throws EvaluationException {
        IDictionary<String, IValue> symbolTable = state.getSymTable();

        if (symbolTable.containsKey(name)) {
            throw new EvaluationException(String.format("Variable %s has already been defined!", name));
        }

        symbolTable.put(name, type.getDefault());

        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws EvaluationException {
        typeEnv.put(name, type);
        return typeEnv;
    }

    @Override
    public String toString() {
        return String.format("%s %s", type.toString(), name);
    }
}
