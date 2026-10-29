classDiagram
    class Patient {
        -String name
        +bookAppointment()
        +countUpcoming()
    }

    class Doctor {
        -String name
        +getAvailableSlots()
        +respond()
    }

    class Appointment {
        -String appointmentId
        -String status
        +submit()
    }

    class TimeSlot {
        -String day
        -String time
        -Boolean isAvailable
        +isFree()
    }

    Patient "1" --> "0..*" Appointment : books
    Doctor "1" --> "0..*" Appointment : receives
    Doctor "1" *-- "0..*" TimeSlot : has
    Appointment "0..1" --> "1" TimeSlot : scheduled for
