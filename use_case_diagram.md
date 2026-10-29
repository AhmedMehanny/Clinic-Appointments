flowchart LR
    P([Patient])
    D([Doctor])

    subgraph Clinic
        UC1[UC1 View availability]
        UC2[UC2 Book appointment]
        UC3[UC3 Accept or decline appointment]
        UC4[UC4 Check appointment limit]
        UC5[UC5 Notify patient of decision]
    end

    P --- UC1
    P --- UC2
    UC3 --- D
    UC4 -.->|"«extend»"| UC2
    UC5 -.->|"«extend»"| UC3



    
