Qelfos = int(input())
cont = 0 
TBPresente = 0
TAPresente = 0 
TMPresente = 0 
TDPresente = 0 
BSobra = 0 
ASobra = 0
MSobra = 0
DSobra = 0


while cont != Qelfos:
    NSH = input().split() 
    Nome = NSH[0]
    Setor = NSH[1].lower()
    Horas = int(NSH[2])
    BPresente = Horas
    APresente = Horas
    MPresente = Horas
    DPresente = Horas

   
    if Setor == 'bonecos':
        while BPresente >= 0:
            BPresente -= 8
            if BPresente >= 0:
                TBPresente += 1
        
       
        if BPresente < 0:
            BSobra = BSobra + (BPresente + 8)
        
    elif Setor == 'arquitetos':
        while APresente >= 0:
            APresente -= 4
            if APresente >= 0:
                TAPresente += 1
        
        if APresente < 0:
            ASobra = ASobra + (APresente + 4)

    elif Setor == 'musicos':
        while MPresente >= 0:
            MPresente -= 6 
            if MPresente >= 0:
                TMPresente += 1
        
        if MPresente < 0:
            MSobra = MSobra + (MPresente + 6)
    
    elif Setor == 'desenhistas':
        while DPresente >= 0:
            DPresente -= 12
            if DPresente >= 0:
                TDPresente += 1
        
        if DPresente < 0:
            DSobra = DSobra + (DPresente + 12)


    cont += 1


if BSobra >= 8:
    while BSobra >= 0:
        BSobra -= 8 
        if BSobra >= 0:
            TBPresente += 1

if ASobra >= 4:
    while ASobra >= 0:
        ASobra -= 4
        if ASobra >= 0:
            TAPresente += 1
    
if MSobra >= 6:
    while MSobra >= 0:
        MSobra -= 6
        if MSobra >= 0:
            TMPresente += 1
    
if DSobra >= 12:
    while DSobra >= 0:
        DSobra -= 12
        if DSobra >= 0:
            TDPresente += 1

print(TBPresente + TAPresente + TMPresente + TDPresente)
