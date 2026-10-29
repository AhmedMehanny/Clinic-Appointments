sequenceDiagram
    participant Patient
    participant Appointment
    participant TimeSlot
    participant Doctor

    Patient->>Patient: bookAppointment()
    Patient->>Patient: countUpcoming()

    alt count >= N (N = 3)
        Patient-->>Patient: LIMIT_REACHED
    else count < N
        Patient->>Appointment: submit()
        Appointment->>TimeSlot: isFree()
        alt Slot is taken
            TimeSlot-->>Appointment: SLOT_TAKEN
        else Slot is free
            Appointment->>Doctor: respond(appointment)
            alt Doctor declines
                Doctor-->>Appointment: DECLINED
            else Doctor accepts
                Doctor-->>Appointment: CONFIRMED
            end
        end
    end
