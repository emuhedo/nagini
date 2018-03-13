"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""

from typing import List, Tuple


Expr = 'silver.ast.Exp'

Stmt = 'silver.ast.Stmt'

StmtsAndExpr = Tuple[List[Stmt], Expr]

VarDecl = 'silver.ast.LocalVarDecl'

Domain = 'silver.ast.Domain'

DomainFuncApp = 'silver.ast.DomainFuncApp'

Predicate = 'silver.ast.Predicate'

Program = 'silver.ast.Program'

Field = 'silver.ast.Field'

Function = 'silver.ast.Function'

Method = 'silver.ast.Method'

FuncApp = 'silver.ast.FuncApp'

TypeVar = 'silver.ast.TypeVar'

Type = 'silver.ast.Type'

Position = 'silver.ast.Position'

Info = 'silver.ast.Info'

Node = 'silver.ast.Node'
