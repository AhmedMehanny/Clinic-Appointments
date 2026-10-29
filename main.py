N = 3


class TimeSlot:
    def __init__(self, day, time, isAvailable=True):
        self.day = day
        self.time = time
        self.isAvailable = isAvailable

    def isFree(self):
        return self.isAvailable


class Doctor:
    def __init__(self, name, timeSlots):
        self.name = name
        self.timeSlots = list(timeSlots)

    def getAvailableSlots(self):
        return [slot for slot in self.timeSlots if slot.isFree()]

    def respond(self, appointment):
        # Fixed rule: the doctor declines appointments on Fridays.
        return appointment.timeSlot.day.lower() != "friday"


class Appointment:
    def __init__(self, appointmentId, patient, doctor, timeSlot):
        self.appointmentId = appointmentId
        self.status = "PENDING"
        self.patient = patient
        self.doctor = doctor
        self.timeSlot = timeSlot

    def submit(self):
        # First, check whether the selected slot is free.
        if not self.timeSlot.isFree():
            self.status = "SLOT_TAKEN"
            return self.status

        # Only ask the doctor if the slot is available.
        if self.doctor.respond(self):
            self.status = "CONFIRMED"
            self.timeSlot.isAvailable = False
        else:
            self.status = "DECLINED"
            # The slot remains available if the doctor declines.

        return self.status


class Patient:
    def __init__(self, name):
        self.name = name
        self.appointments = []

    def countUpcoming(self):
        return sum(
            1 for appointment in self.appointments
            if appointment.status == "CONFIRMED"
        )

    def bookAppointment(self, doctors, appointmentId, doctorName, day, time):
        # Check the appointment limit first.
        if self.countUpcoming() >= N:
            return "LIMIT_REACHED"

        # Reject an unknown doctor.
        doctor = next(
            (d for d in doctors if d.name == doctorName),
            None
        )
        if doctor is None:
            return "UNKNOWN_DOCTOR"

        # Only accept slots owned by the selected doctor.
        timeSlot = next(
            (
                slot for slot in doctor.timeSlots
                if slot.day.lower() == day.lower()
                and slot.time == time
            ),
            None
        )
        if timeSlot is None:
            return "UNKNOWN_SLOT"

        # Submit the appointment: check the slot, then ask the doctor.
        appointment = Appointment(
            appointmentId, self, doctor, timeSlot
        )
        self.appointments.append(appointment)

        return appointment.submit()


def main():
    # The doctor owns these time slots.
    doctor = Doctor(
        "Dr. Smith",
        [
            TimeSlot("Monday", "09:00"),
            TimeSlot("Tuesday", "10:00"),
            TimeSlot("Wednesday", "11:00"),
            TimeSlot("Thursday", "12:00"),
            TimeSlot("Friday", "13:00"),
            TimeSlot("Saturday", "14:00"),
        ]
    )
    doctors = [doctor]

    # Scenario 1: A successful booking.
    patient1 = Patient("Alice")
    status1 = patient1.bookAppointment(
        doctors, "A001", "Dr. Smith", "Monday", "09:00"
    )
    print(f"CONFIRMED scenario: {status1}")

    # Scenario 2: The doctor declines the appointment.
    patient2 = Patient("Bob")
    status2 = patient2.bookAppointment(
        doctors, "A002", "Dr. Smith", "Friday", "13:00"
    )
    print(f"DECLINED scenario: {status2}")

    # Scenario 3: The slot was already booked by Alice.
    patient3 = Patient("Charlie")
    status3 = patient3.bookAppointment(
        doctors, "A003", "Dr. Smith", "Monday", "09:00"
    )
    print(f"SLOT_TAKEN scenario: {status3}")

    # Scenario 4: Three confirmed appointments, then one more attempt.
    patient4 = Patient("Dana")

    limit_setup_statuses = [
        patient4.bookAppointment(
            doctors, "A004", "Dr. Smith", "Tuesday", "10:00"
        ),
        patient4.bookAppointment(
            doctors, "A005", "Dr. Smith", "Wednesday", "11:00"
        ),
        patient4.bookAppointment(
            doctors, "A006", "Dr. Smith", "Thursday", "12:00"
        ),
    ]

    limit_status = patient4.bookAppointment(
        doctors, "A007", "Dr. Smith", "Saturday", "14:00"
    )

    print(
        "LIMIT_REACHED scenario: "
        + ", ".join(limit_setup_statuses)
        + f" -> {limit_status}"
    )


if __name__ == "__main__":
    main()
