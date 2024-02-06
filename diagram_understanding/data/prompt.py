prompt_geometry3k_long = '''
Logic_form = 
""" 
{
  "text_logic_form": [
    "Congruent(Triangle(R,S,T),Triangle(X,Y,Z))",
    "Find(y)"
  ],
  "dissolved_text_logic_form": [
    "Congruent(Triangle(R,S,T),Triangle(X,Y,Z))",
    "Find(y)"
  ],
  "diagram_logic_form": [
    "Equals(LengthOf(Line(T, R)), x+21)",
    "Equals(MeasureOf(Angle(T, R, S)), 4y-10)",
    "Equals(MeasureOf(Angle(Z, X, Y)), 3y+5)",
    "Equals(LengthOf(Line(Z, X)), 2x-14)"
  ],
  "line_instances": [
    "SR",
    "ST",
    "TR",
    "XY",
    "XZ",
    "ZY"
  ],
  "point_positions": {
    "R": [
      2.0,
      56.0
    ],
    "S": [
      55.0,
      223.0
    ],
    "T": [
      321.0,
      3.0
    ],
    "X": [
      600.0,
      120.0
    ],
    "Y": [
      550.0,
      -30.0
    ],
    "Z": [
      321.0,
      180.0
    ]
  },
  "circle_instances": [
    ""
  ]
}
"""

---

Natural_form = 
"""
{
  "text_logic_form": [
    "The triangles $RST$ and $XYZ$ are congruent to each other.",
    "Find $y$."
  ],
  "dissolved_text_logic_form": [
    "The triangles $RST$ and $XYZ$ are congruent to each other.",
    "Find $y$."
  ],
  "diagram_logic_form": [
    "The length of the line $TR$ is $x+21$.",
    "The measure of angle $TRS$ is $4y - 10$ degrees.",
    "The measure of angle $ZXY$ is $3y+5$ degrees.",
    "The length of the line $ZX$ is $2x-14$."
  ],
  "line_instances": [
    "There are lines $SR$, $ST$, $TR$, forming a triangle $TRS$.",
    "There are lines $XY$, $XZ$, $ZY$, forming a triangle $XYZ$."
  ],
  "point_positions": {
    "R": "Point R is positioned at (2.0, 56.0).",
    "S": "Point S is positioned at (55.0, 223.0).",
    "T": "Point T is positioned at (321.0, 3.0).",
    "X": "Point X is positioned at (600.0, 120.0).",
    "Y": "Point Y is positioned at (550.0, -30.0).",
    "Z": "Point Z is positioned at (321.0, 180.0)."
  },
  "circle_instances": [
    ""
  ]
}
"""

Logic_form = 
"""
{
  "text_logic_form": [
    "Parallelogram(M,N,P,R)",
    "Find(y)"
  ],
  "dissolved_text_logic_form": [
    "Parallelogram(M,N,P,R)",
    "Find(y)"
  ],
  "diagram_logic_form": [
    "Equals(LengthOf(Line(P, Q)), 11.1)",
    "Equals(MeasureOf(Angle(N, Q, P)), 83)",
    "Equals(LengthOf(Line(R, P)), 20)",
    "Equals(LengthOf(Line(M, N)), 3x-4)",
    "Equals(LengthOf(Line(P, N)), 2y+5)",
    "Equals(LengthOf(Line(N, Q)), 15.4)",
    "Equals(MeasureOf(Angle(Q, N, M)), 33)",
    "Equals(LengthOf(Line(M, N)), 3x-4)",
    "Equals(LengthOf(Line(R, Q)), 3z-3)",
    "Equals(MeasureOf(Angle(M, R, Q)), 38)",
    "Equals(LengthOf(Line(R, M)), 17.9)",
    "PointLiesOnLine(Q, Line(R, N))",
    "PointLiesOnLine(Q, Line(P, M))"
  ],
  "line_instances": [
    "MN",
    "MQ",
    "NQ",
    "PM",
    "PN",
    "PQ",
    "RM",
    "RN",
    "RP",
    "RQ"
  ],
  "point_positions": {
    "M": [
      65.0,
      0.0
    ],
    "N": [
      260.0,
      1.0
    ],
    "P": [
      197.0,
      166.0
    ],
    "Q": [
      131.0,
      83.0
    ],
    "R": [
      0.0,
      166.0
    ]
  },
  "circle_instances": [
    ""
  ]
}
"""

Natural_form = {
  "text_logic_form": [
    "The figure $MNPQ$ is a parallelogram.",
    "Find $y$."
  ],
  "dissolved_text_logic_form": [
    "The figure $MNPQ$ is a parallelogram.",
    "Find $y$."
  ],
  "diagram_logic_form": [
    "The length of the line $PQ$ is $11.1$ units.",
    "The measure of angle $NQP$ is $83$ degrees.",
    "The length of the line $RP$ is $20$.",
    "The length of the line $MN$ is $3x - 4$.",
    "The length of the line $PN$ is $2y + 5$.",
    "The length of the line $NQ$ is $15.4$.",
    "The measure of angle $QNM$ is $33$ degrees.",
    "The length of the line $MN$ is repeated as $3x - 4$.",
    "The length of the line $RQ$ is $3z - 3$.",
    "The measure of angle $MRQ$ is $38$ degrees.",
    "The length of the line $RM$ is $17.9$.",
    "Point $Q$ lies on the line connecting $R$ and $N$.",
    "Point $Q$ also lies on the line connecting $P$ and $M$."
  ],
  "line_instances": [
    "There are lines $MN$, $PN$, $RM$, and $RN$, forming the parallelogram and its diagonals.",
    "The lines $MP$, $MQ$, and $QM$ are colinear.",
    "The lines $RN$, $RQ$, and $QN$ are colinear.",
    "The line $MP$ and $RN$ are the diagonals of the parallelogram $MNPR$"
  ],
  "point_positions": {
    "M": "Point M is positioned at (65.0, 0.0).",
    "N": "Point N is at (260.0, 1.0).",
    "P": "Point P is positioned at (197.0, 166.0).",
    "Q": "Point Q is at (131.0, 83.0).",
    "R": "Point R lives at (0.0, 166.0)."
  },
  "circle_instances": [
    ""
  ]
}
"""

---

Logic_form = 
"""
{
  "text_logic_form": [
    "IsMedianOf(Line(J,K),Quadrilateral(A,B,T,Q))",
    "Find(LengthOf(Line(J,K)))"
  ],
  "dissolved_text_logic_form": [
    "IsMedianOf(Line(J,K),Quadrilateral(A,B,T,Q))",
    "Find(LengthOf(Line(J,K)))"
  ],
  "diagram_logic_form": [
    "Equals(LengthOf(Line(Q, T)), 86)",
    "Equals(LengthOf(Line(R, S)), 54)",
    "PointLiesOnLine(A, Line(R, Q))",
    "PointLiesOnLine(B, Line(S, T))",
    "Equals(LengthOf(Line(Q, A)), LengthOf(Line(R, A)))",
    "Equals(LengthOf(Line(B, T)), LengthOf(Line(S, B)))"
  ],
  "line_instances": [
    "AB",
    "BT",
    "QA",
    "QT",
    "RA",
    "RQ",
    "RS",
    "SB",
    "ST"
  ],
  "point_positions": {
    "A": [
      17.0,
      34.0
    ],
    "B": [
      245.0,
      35.0
    ],
    "Q": [
      0.0,
      65.0
    ],
    "R": [
      36.0,
      2.0
    ],
    "S": [
      211.0,
      2.0
    ],
    "T": [
      274.0,
      64.0
    ]
  },
  "circle_instances": [
    ""
  ]
}
"""

Natural_form = 
"""
{
  "text_logic_form": [
    "The line $JK$ is a median of the quadrilateral $ABTQ$.",
    "Find the length of the line $JK$."
  ],
  "dissolved_text_logic_form": [
    "The line $JK$ is a median of the quadrilateral $ABTQ$.",
    "Find the length of the line $JK$."
  ],
  "diagram_logic_form": [
    "The length of the line $QT$ is $86$.",
    "The length of the line $RS$ is $54$.",
    "Point $A$ lies on the line connecting $R$ and $Q$.",
    "Point $B$ lies on the line connecting $S$ and $T$.",
    "The length of the line from $Q$ to $A$ is equal to the length of the line from $R$ to $A$.",
    "The length of the line from $B$ to $T$ is equal to the length of the line from $S$ to $B$."
  ],
  "line_instances": [
    "There are lines $AB$, $BT$, $QA$, $QT$, $RA$, $RQ$, $RS$, $SB$, and $ST$, forming the quadrilateral and associated lines."
  ],
  "point_positions": {
    "A": "Point A is positioned at (17.0, 34.0).",
    "B": "Point B is at (245.0, 35.0).",
    "Q": "Point Q is at (0.0, 65.0).",
    "R": "Point R is positioned at (36.0, 2.0).",
    "S": "Point S is at (211.0, 2.0).",
    "T": "Point T is positioned at (274.0, 64.0)."
  },
  "circle_instances": [
    ""
  ]
}
"""

--- 

Logic_form = 
"""
<INPUT>
"""

Natural_form =

'''
#input : <INPUT>

prompt_geometry3k = '''
Generate the corresponding natural form based on the following examples. Use precise but creative and diverse expressions to illustrate.

Logic_form = 
""" 
{
  "text_logic_form": [
    "Congruent(Triangle(R,S,T),Triangle(X,Y,Z))",
    "Find(y)"
  ],
  "dissolved_text_logic_form": [
    "Congruent(Triangle(R,S,T),Triangle(X,Y,Z))",
    "Find(y)"
  ],
  "diagram_logic_form": [
    "Equals(LengthOf(Line(T, R)), x+21)",
    "Equals(MeasureOf(Angle(T, R, S)), 4y-10)",
    "Equals(MeasureOf(Angle(Z, X, Y)), 3y+5)",
    "Equals(LengthOf(Line(Z, X)), 2x-14)"
  ],
  "line_instances": [
    "SR",
    "ST",
    "TR",
    "XY",
    "XZ",
    "ZY"
  ],
  "point_positions": {
    "R": [
      2.0,
      56.0
    ],
    "S": [
      55.0,
      223.0
    ],
    "T": [
      321.0,
      3.0
    ],
    "X": [
      600.0,
      120.0
    ],
    "Y": [
      550.0,
      -30.0
    ],
    "Z": [
      321.0,
      180.0
    ]
  },
  "circle_instances": [
    ""
  ]
}
"""

---

Natural_form = 
"""
{
  "text_logic_form": [
    "The triangles $RST$ and $XYZ$ are congruent to each other.",
    "Find $y$."
  ],
  "dissolved_text_logic_form": [
    "The triangles $RST$ and $XYZ$ are congruent to each other.",
    "Find $y$."
  ],
  "diagram_logic_form": [
    "The length of the line $TR$ is $x+21$.",
    "The measure of angle $TRS$ is $4y - 10$ degrees.",
    "The measure of angle $ZXY$ is $3y+5$ degrees.",
    "The length of the line $ZX$ is $2x-14$."
  ],
  "line_instances": [
    "There are lines $SR$, $ST$, $TR$, forming a triangle $TRS$.",
    "There are lines $XY$, $XZ$, $ZY$, forming a triangle $XYZ$."
  ],
  "point_positions": {
    "R": "Point R is positioned at (2.0, 56.0).",
    "S": "Point S is positioned at (55.0, 223.0).",
    "T": "Point T is positioned at (321.0, 3.0).",
    "X": "Point X is positioned at (600.0, 120.0).",
    "Y": "Point Y is positioned at (550.0, -30.0).",
    "Z": "Point Z is positioned at (321.0, 180.0)."
  },
  "circle_instances": [
    ""
  ]
}
"""

Logic_form = 
"""
{
  "text_logic_form": [
    "Parallelogram(M,N,P,R)",
    "Find(y)"
  ],
  "dissolved_text_logic_form": [
    "Parallelogram(M,N,P,R)",
    "Find(y)"
  ],
  "diagram_logic_form": [
    "Equals(LengthOf(Line(P, Q)), 11.1)",
    "Equals(MeasureOf(Angle(N, Q, P)), 83)",
    "Equals(LengthOf(Line(R, P)), 20)",
    "Equals(LengthOf(Line(M, N)), 3x-4)",
    "Equals(LengthOf(Line(P, N)), 2y+5)",
    "Equals(LengthOf(Line(N, Q)), 15.4)",
    "Equals(MeasureOf(Angle(Q, N, M)), 33)",
  ],
  "line_instances": [
    "MN",
    "MQ",
    "NQ",
    "PM",
    "PN",
    "PQ",
    "RM",
    "RN",
    "RP",
    "RQ"
  ],
  "point_positions": {
    "M": [
      65.0,
      0.0
    ],
    "N": [
      260.0,
      1.0
    ],
    "P": [
      197.0,
      166.0
    ]
    ]
  },
  "circle_instances": [
    ""
  ]
}
"""

Natural_form = {
  "text_logic_form": [
    "The figure $MNPQ$ is a parallelogram.",
    "Find $y$."
  ],
  "dissolved_text_logic_form": [
    "The figure $MNPQ$ is a parallelogram.",
    "Find $y$."
  ],
  "diagram_logic_form": [
    "The length of the line $PQ$ is $11.1$.",
    "The measure of angle $NQP$ is $83$ degrees.",
    "The length of the line $RP$ is $20$.",
    "The length of the line $MN$ is $3x - 4$.",
    "The length of the line $PN$ is $2y + 5$s.",
    "The length of the line $NQ$ is $15.4$ units.",
    "The measure of angle $QNM$ is $33$ degrees.",
  ],
  "line_instances": [
    "There are lines $MN$, $PN$, $RM$, and $RN$, forming the parallelogram and its diagonals.",
    "The lines $MP$, $MQ$, and $QM$ are colinear.",
    "The lines $RN$, $RQ$, and $QN$ are colinear.",
    "The line $MP$ and $RN$ are the diagonals of the parallelogram $MNPR$"
  ],
  "point_positions": {
    "M": "Point M is at (65.0, 0.0).",
    "N": "Point N is at (260.0, 1.0).",
    "P": "Point P is positioned at (197.0, 166.0).",
  },
  "circle_instances": [
    ""
  ]
}
"""

--- 

Logic_form = 
"""
<INPUT>
"""

Natural_form =

'''
#input : <INPUT>