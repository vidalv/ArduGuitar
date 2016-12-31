# defaultPresets.py

defPresetDict  = {(0,0): {'Name':'(0,0) seq-0','M' : [5,5],'A' : [5,5],'B' : [5,5],'C' : [5,5],'D' : [5,5],'TR' : [None,5],'S' : '(+AB)',        'TREM' : 0,'VIB' : 0, 'AUX0' : 0, 'AUX1' : 0, 'SEQ' : 0 },
                  (0,1): {'Name':'(0,1)',      'M' : [5,5],'A' : [5,5],'B' : [5,5],'C' : [5,5],'D' : [5,5],'TR' : [None,5],'S' : '(|AB)',        'TREM' : 0,'VIB' : 0, 'AUX0' : 0, 'AUX1' : 0, 'SEQ' : ''},
                  (0,2): {'Name':'(0,2) seq-1','M' : [5,5],'A' : [5,5],'B' : [5,5],'C' : [5,5],'D' : [5,5],'TR' : [None,5],'S' : '(|(+AB)(+CD))','TREM' : 0,'VIB' : 0, 'AUX0' : 0, 'AUX1' : 0, 'SEQ' : 1 },
                  (0,3): {'Name':'(0,3)',      'M' : [5,5],'A' : [5,5],'B' : [5,5],'C' : [5,5],'D' : [5,5],'TR' : [None,5],'S' : '(|CD)',        'TREM' : 0,'VIB' : 0, 'AUX0' : 0, 'AUX1' : 0, 'SEQ' : ''},
                  (0,4): {'Name':'(0,4) seq-2','M' : [5,5],'A' : [5,5],'B' : [5,5],'C' : [5,5],'D' : [5,5],'TR' : [None,5],'S' : '(+CD)',        'TREM' : 0,'VIB' : 0, 'AUX0' : 0, 'AUX1' : 0, 'SEQ' : 2 },

                  (1,0): {'Name':'(1,0)',      'M' : [5,5],'A' : [5,5],'B' : [5,5],'C' : [5,5],'D' : [5,5],'TR' : [None,5],'S' : '(|AB)',        'TREM' : 0,'VIB' : 0, 'AUX0' : 0, 'AUX1' : 0, 'SEQ' : ''},
                  (1,1): {'Name':'(1,1)',      'M' : [5,5],'A' : [5,5],'B' : [5,5],'C' : [5,5],'D' : [5,5],'TR' : [None,5],'S' : '(+(|AB)C)',    'TREM' : 0,'VIB' : 0, 'AUX0' : 0, 'AUX1' : 0, 'SEQ' : ''},
                  (1,2): {'Name':'(1,2)',      'M' : [5,5],'A' : [5,5],'B' : [5,5],'C' : [5,5],'D' : [5,5],'TR' : [None,5],'S' : '(|ABCD)',      'TREM' : 0,'VIB' : 0, 'AUX0' : 0, 'AUX1' : 0, 'SEQ' : ''},
                  (1,3): {'Name':'(1,3)',      'M' : [5,5],'A' : [5,5],'B' : [5,5],'C' : [5,5],'D' : [5,5],'TR' : [None,5],'S' : '(+B(|CD))',    'TREM' : 0,'VIB' : 0, 'AUX0' : 0, 'AUX1' : 0, 'SEQ' : ''},
                  (1,4): {'Name':'(1,4)',      'M' : [5,5],'A' : [5,5],'B' : [5,5],'C' : [5,5],'D' : [5,5],'TR' : [None,5],'S' : '(|CD)',        'TREM' : 0,'VIB' : 0, 'AUX0' : 0, 'AUX1' : 0, 'SEQ' : ''},

                  (2,0): {'Name':'(2,0)',      'M' : [5,5],'A' : [5,5],'B' : [5,5],'C' : [5,5],'D' : [5,5],'TR' : [None,5],'S' : '(|AC)',        'TREM' : 0,'VIB' : 0, 'AUX0' : 0, 'AUX1' : 0, 'SEQ' : ''},
                  (2,1): {'Name':'(2,1)',      'M' : [5,5],'A' : [5,5],'B' : [5,5],'C' : [5,5],'D' : [5,5],'TR' : [None,5],'S' : '(|AD)',        'TREM' : 0,'VIB' : 0, 'AUX0' : 0, 'AUX1' : 0, 'SEQ' : ''},
                  (2,2): {'Name':'(2,2)',      'M' : [5,5],'A' : [5,5],'B' : [5,5],'C' : [5,5],'D' : [5,5],'TR' : [None,5],'S' : '(|ABC)',       'TREM' : 0,'VIB' : 0, 'AUX0' : 0, 'AUX1' : 0, 'SEQ' : ''},
                  (2,3): {'Name':'(2,3)',      'M' : [5,5],'A' : [5,5],'B' : [5,5],'C' : [5,5],'D' : [5,5],'TR' : [None,5],'S' : '(|BC)',        'TREM' : 0,'VIB' : 0, 'AUX0' : 0, 'AUX1' : 0, 'SEQ' : ''},
                  (2,4): {'Name':'(2,4)',      'M' : [5,5],'A' : [5,5],'B' : [5,5],'C' : [5,5],'D' : [5,5],'TR' : [None,5],'S' : '(|BD)',        'TREM' : 0,'VIB' : 0, 'AUX0' : 0, 'AUX1' : 0, 'SEQ' : ''},

                  (3,0): {'Name':'(3,0)',      'M' : [5,5],'A' : [5,5],'B' : [5,5],'C' : [5,5],'D' : [5,5],'TR' : [None,5],'S' : '(|Ab)',        'TREM' : 0,'VIB' : 0, 'AUX0' : 0, 'AUX1' : 0, 'SEQ' : ''},
                  (3,1): {'Name':'(3,1)',      'M' : [5,5],'A' : [5,5],'B' : [5,5],'C' : [5,5],'D' : [5,5],'TR' : [None,5],'S' : '(|Bc)',        'TREM' : 0,'VIB' : 0, 'AUX0' : 0, 'AUX1' : 0, 'SEQ' : ''},
                  (3,2): {'Name':'(3,2)',      'M' : [5,5],'A' : [5,5],'B' : [5,5],'C' : [5,5],'D' : [5,5],'TR' : [None,5],'S' : '(|BCD)',       'TREM' : 0,'VIB' : 0, 'AUX0' : 0, 'AUX1' : 0, 'SEQ' : ''},
                  (3,3): {'Name':'(3,3)',      'M' : [5,5],'A' : [5,5],'B' : [5,5],'C' : [5,5],'D' : [5,5],'TR' : [None,5],'S' : '(|Cd)',        'TREM' : 0,'VIB' : 0, 'AUX0' : 0, 'AUX1' : 0, 'SEQ' : ''},
                  (3,4): {'Name':'(3,4)',      'M' : [5,5],'A' : [5,5],'B' : [5,5],'C' : [5,5],'D' : [5,5],'TR' : [None,5],'S' : '(|AbcD)',      'TREM' : 0,'VIB' : 0, 'AUX0' : 0, 'AUX1' : 0, 'SEQ' : ''},

                  (4,0): {'Name':'(4,0)',      'M' : [5,5],'A' : [5,5],'B' : [5,5],'C' : [5,5],'D' : [5,5],'TR' : [None,5],'S' : '(|A(+BD)C)',   'TREM' : 0,'VIB' : 0, 'AUX0' : 0, 'AUX1' : 0, 'SEQ' : ''},
                  (4,1): {'Name':'(4,1)',      'M' : [5,5],'A' : [5,5],'B' : [5,5],'C' : [5,5],'D' : [5,5],'TR' : [None,5],'S' : 'A',            'TREM' : 0,'VIB' : 0, 'AUX0' : 0, 'AUX1' : 0, 'SEQ' : ''},
                  (4,2): {'Name':'(4,2)',      'M' : [5,5],'A' : [5,5],'B' : [5,5],'C' : [5,5],'D' : [5,5],'TR' : [None,5],'S' : 'B',            'TREM' : 0,'VIB' : 0, 'AUX0' : 0, 'AUX1' : 0, 'SEQ' : ''},
                  (4,3): {'Name':'(4,3)',      'M' : [5,5],'A' : [5,5],'B' : [5,5],'C' : [5,5],'D' : [5,5],'TR' : [None,5],'S' : 'C',            'TREM' : 0,'VIB' : 0, 'AUX0' : 0, 'AUX1' : 0, 'SEQ' : ''},
                  (4,4): {'Name':'(4,4)',      'M' : [5,5],'A' : [5,5],'B' : [5,5],'C' : [5,5],'D' : [5,5],'TR' : [None,5],'S' : 'D',            'TREM' : 0,'VIB' : 0, 'AUX0' : 0, 'AUX1' : 0, 'SEQ' : ''}
                 }
                  
