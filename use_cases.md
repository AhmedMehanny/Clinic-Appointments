| UC  | Name                        | Actor   | Requirement | Use Case Text                                                                                                      |
|-----|-----------------------------|---------|-------------|-------------------------------------------------------------------------------------------------------------------|
| UC1 | View availability           | Patient | R1          | As Patient I do view the days and times when a doctor is available.                                               |
| UC2 | Book appointment            | Patient | R2          | As Patient I do book an appointment during an available time slot.                                                |
| UC3 | Accept or decline appointment | Doctor  | R3          | As Doctor I do accept or decline an appointment request.                                                          |
| UC4 | Check appointment limit     | System  | R4          | As System I do check that the patient has fewer than 3 upcoming appointments before allowing a new booking.       |
| UC5 | Notify patient of decision  | System  | R3          | As System I do notify the patient of the doctor's decision.                                                       |

UC2 — Book appointment
Main flow
1. Patient selects a doctor.
2. System displays the doctor's available appointment times.
3. Patient selects an available time slot.
4. System checks whether the patient has reached the limit of 3 upcoming appointments.
5. System confirms that the appointment limit has not been reached.
6. System creates an appointment request.
7. Doctor reviews the appointment request.
8. Doctor accepts the request.
9. System confirms the appointment and notifies the patient.


Alternative flow — Doctor declines
1. Doctor reviews the appointment request.
2. Doctor declines the request.
3. System notifies the patient that the request was declined.
4. The appointment is not confirmed.
