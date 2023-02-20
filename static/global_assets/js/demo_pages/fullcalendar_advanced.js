/* ------------------------------------------------------------------------------
 *
 *  # Fullcalendar advanced options
 *
 *  Demo JS code for extra_fullcalendar_advanced.html page
 *
 * ---------------------------------------------------------------------------- */


// Setup module
// ------------------------------

const FullCalendarAdvanced = function() {
    console.log('{{test_tag}}')
    console.log('typeof', initiate_date)
    console.log('typeof', typeof adminChck)
    if(adminChck == "True") {

        console.log('typeof', JSON.parse(records.replace(/&quot;/g, '"')))
        var parsed_events_data = JSON.parse(records.replace(/&quot;/g, '"')).map((obj) => {return{
            title: "",
            start: obj.fields.start_from,
            end: obj.fields.end_at,
            id: obj.pk
        }})
        
    } else {        
        var parsed_events_data = JSON.parse(records.replace(/&quot;/g, '"')).map((obj) => {return{
            title: `${obj.employee.emp_full_name} | ${obj.employee.emp_full_name_ar} | ${obj.shift.shift_title} - ${obj.shift.shift_type} | ${obj.shift.start_time} - ${obj.shift.end_time} `,
            start: obj.day,
        }})
        
        console.log('typeof', JSON.parse(records.replace(/&quot;/g, '"')))
    }

    //
    // Setup module components
    //

    // External events
    const _componentFullCalendarEvents = function() {
        if (typeof FullCalendar == 'undefined') {
            console.warn('Warning - Fullcalendar is not loaded.');
            return;
        }
        // console.log('{{test_tag}}')
        // console.log('typeof', initiate_date)
        // var parsed_events_data = JSON.parse(records.replace(/&quot;/g, '"')).map((obj) => {return{
        //     title: "test",
        //     start: obj.fields.start_from,
        //     end: obj.fields.end_at,
        // }})
        // console.log('typeof', parsed_events_data)


        // Add demo events
        // ------------------------------

        // Default events
        // const events = [
        //     {
        //         title: 'All Day Event',
        //         start: '2020-09-01'
        //     },
        //     {
        //         title: 'Long Event',
        //         start: '2020-09-07',
        //         end: '2020-09-10'
        //     },
        //     {
        //         groupId: 999,
        //         title: 'Repeating Event',
        //         start: '2020-09-09T16:00:00'
        //     },
        //     {
        //         groupId: 999,
        //         title: 'Repeating Event',
        //         start: '2020-09-16T16:00:00'
        //     },
        //     {
        //         title: 'Conference',
        //         start: '2020-09-11',
        //         end: '2020-09-13'
        //     },
        //     {
        //         title: 'Meeting',
        //         start: '2020-09-12T10:30:00',
        //         end: '2020-09-12T12:30:00'
        //     },
        //     {
        //         title: 'Lunch',
        //         start: '2020-09-12T12:00:00'
        //     },
        //     {
        //         title: 'Meeting',
        //         start: '2020-09-12T14:30:00'
        //     },
        //     {
        //         title: 'Happy Hour',
        //         start: '2020-09-12T17:30:00'
        //     },
        //     {
        //         title: 'Dinner',
        //         start: '2020-09-12T20:00:00'
        //     },
        //     {
        //         title: 'Birthday Party',
        //         start: '2020-09-13T07:00:00'
        //     },
        //     {
        //         title: 'Click for Google',
        //         url: 'http://google.com/',
        //         start: '2020-09-28'
        //     }
        // ];

        const events = parsed_events_data;

        //
        // External events
        //

        // Define components
        const calendarEventsContainerElement = document.getElementById('external-events-list');
        const calendarEventsElement = document.querySelector('.fullcalendar-external');
        const checkboxElement = document.getElementById('drop-remove');

        // Initialize
        if(calendarEventsElement) {

            // Use custom colors for external events
            const eventColors = calendarEventsContainerElement.querySelectorAll('.fc-event');
            eventColors.forEach(function(element) {
                element.style.borderColor = element.getAttribute('data-color');
                element.style.backgroundColor = element.getAttribute('data-color');
            });

            // Initialize the external events
            new FullCalendar.Draggable(calendarEventsContainerElement, {
                itemSelector: '.fc-event',
                eventData: function(eventEl) {
                    return {
                        title: eventEl.innerText.trim(),
                        backgroundColor: eventEl.getAttribute('data-color'),
                        borderColor: eventEl.getAttribute('data-color')
                    }
                }
            });

            // Initialize the calendar
            const calendarEventsInit = new FullCalendar.Calendar(calendarEventsElement, {
                headerToolbar: {
                    left: 'prev,next today',
                    center: 'title',
                    right: 'dayGridMonth,timeGridWeek,timeGridDay,listWeek'
                },
                editable: true,
                droppable: true, // this allows things to be dropped onto the calendar
                initialDate: '2020-09-12',
                direction: document.dir == 'rtl' ? 'rtl' : 'ltr',
                events: events,
                drop: function(arg) {
                    if (checkboxElement.checked) {
                        arg.draggedEl.parentNode.removeChild(arg.draggedEl);
                    }
                }
            });

            // Init
            calendarEventsInit.render();

            // Resize calendar when sidebar toggler is clicked
            $('.sidebar-control').on('click', function() {
                calendarEventsInit.updateSize();
            });
        }
    };

    // FullCalendar RTL direction
    const _componentFullCalendarSelectable = function() {
        if (typeof FullCalendar == 'undefined') {
            console.warn('Warning - Fullcalendar files are not loaded.');
            return;
        }

        function fillZero(num) {
            if (num.toString().length == 1) {
                return `0${num}`
            } else {
                return `${num}`
            }
        }

        // Add demo events
        // ------------------------------

        // Default events
        // const events = [
        //     {
        //         title: 'All Day Event',
        //         start: '2020-09-01'
        //     },
        //     {
        //         title: 'Long Event',
        //         start: '2020-09-07',
        //         end: '2020-09-10'
        //     },
        //     {
        //         groupId: 999,
        //         title: 'Repeating Event',
        //         start: '2020-09-09T16:00:00'
        //     },
        //     {
        //         groupId: 999,
        //         title: 'Repeating Event',
        //         start: '2020-09-16T16:00:00'
        //     },
        //     {
        //         title: 'Conference',
        //         start: '2020-09-11',
        //         end: '2020-09-13'
        //     },
        //     {
        //         title: 'Meeting',
        //         start: '2020-09-12T10:30:00',
        //         end: '2020-09-12T12:30:00'
        //     },
        //     {
        //         title: 'Lunch',
        //         start: '2020-09-12T12:00:00'
        //     },
        //     {
        //         title: 'Meeting',
        //         start: '2020-09-12T14:30:00'
        //     },
        //     {
        //         title: 'Happy Hour',
        //         start: '2020-09-12T17:30:00'
        //     },
        //     {
        //         title: 'Dinner',
        //         start: '2020-09-12T20:00:00'
        //     },
        //     {
        //         title: 'Birthday Party',
        //         start: '2020-09-13T07:00:00'
        //     },
        //     {
        //         title: 'Click for Google',
        //         url: 'http://google.com/',
        //         start: '2020-09-28'
        //     }
        // ];

        const events = parsed_events_data;

        //
        // Selectable
        //

        // Define element
        const calendarSelectableElement = document.querySelector('.fullcalendar-selectable');

        // Initialize
        if(calendarSelectableElement) {
            const calendarSelectableInit = new FullCalendar.Calendar(calendarSelectableElement, {
                headerToolbar: {
                        // left: 'none',
                        // center: 'title',
                        right: 'dayGridMonth,timeGridWeek,timeGridDay'
                },
                // initialDate: '2020-09-12',
                initialDate: initiate_date,
                navLinks: false, // can click day/week names to navigate views
                selectable: true,
                selectMirror: true,
                events: events,
                select: function(arg) {
                    // const title = prompt('Event Title:');
                    console.log('typeof', typeof arg.start)
                    console.log('typeof', arg.start.getFullYear())
                    console.log('typeof', arg.start.getMonth())
                    console.log('typeof', arg.start.getDate())
                    console.log('typeof', arg.start.getHours())
                    console.log('typeof', arg.start.getMinutes())
                    console.log('typeof', arg.start.getSeconds())
                    console.log('typeof', test_tag)
                    // let startDateTime = `${fillZero(arg.start.getFullYear())}-${fillZero(arg.start.getMonth())}-${fillZero(arg.start.getDate())} ${fillZero(arg.start.getHours())}:${fillZero(arg.start.getMinutes())}:${fillZero(arg.start.getSeconds())}`
                    let startDateTime = `${fillZero(arg.start.getFullYear())}-${fillZero(arg.start.getMonth()+1)}-${fillZero(arg.start.getDate())}`
                    // let endDateTime = `${fillZero(arg.end.getFullYear())}-${fillZero(arg.end.getMonth())}-${fillZero(arg.end.getDate())} ${fillZero(arg.end.getHours())}:${fillZero(arg.end.getMinutes())}:${fillZero(arg.end.getSeconds())}`
                    let endDateTime = `${fillZero(arg.end.getFullYear())}-${fillZero(arg.end.getMonth()+1)}-${fillZero(arg.end.getDate())}`
                    // 2022-12-31 23:59:59
                    if(adminChck == "True") {
                        document.getElementById('event-creation-form').style.display = 'flex';
                        document.getElementById('id_start_from').value = startDateTime;
                        document.getElementById('id_end_at').value = endDateTime;
                    }
                    
                    // if (title) {
                        // calendarSelectableInit.addEvent({
                        //     title: "",
                        //     start: arg.start,
                        //     end: arg.end,
                        //     allDay: arg.allDay
                        // });
                    // }
                    // calendarSelectableInit.unselect();
                },
                eventClick: function(arg) {
                    if(adminChck == "True") {

                    // $(document).ready(function() {
                        $('#example').DataTable( {
                            columns: [
                                { data: 'day' },
                                { data: 'employee' },
                                { data: 'employee_id' }
                            ],
                            ajax: {
                                url: url,
                                type: "POST",
                                headers: {
                                    'Content-Type': 'application/json',
                                    'Accept': 'application/json',
                                    'X-CSRFToken': csrfmiddlewaretoken
                                },
                                data: function() {
                                    return JSON.stringify({val: arg.event._def.publicId});
                                },
                                dataSrc: function ( json ) {
                                    // Manipulate the JSON data if needed
                                    console.log('json', json)
                                    document.getElementById('shift-title').innerHTML += json[0] !== undefined && json[0] !== null ? json[0]['shift']['shift_title']: '';
                                    document.getElementById('shift-type').innerHTML += json[0] !== undefined && json[0] !== null ? json[0]['shift']['shift_type']: '';
                                    if(json[0]['shift']['shift_type'] !== 'Split'){
                                        let html = `
                                        <li>
                                            <i class="icon-checkmark-circle text-success mr-2"></i>
                                            START <span>${json[0]['shift']['start_time']}</span> 
                                            END <span>${json[0]['shift']['end_time']}</span> 
                                        </li>
                                        `;
                                        document.getElementById('shift-log').innerHTML += html;
                                    } else if (json[0]['shift']['shift_type'] === 'Split') {
                                        $.ajax({
                                            type: 'POST',
                                            url: splitShiftTimeSlotsurl,
                                            data: {
                                                csrfmiddlewaretoken: csrfmiddlewaretoken, 
                                                val: json[0]['shift']['id']
                                            },
                                            dataType: 'json',
                                    
                                            success: function(response) {
                                                console.log(response)
                                                response.map(item => {
                                                    document.getElementById('shift-log').innerHTML += `
                                                    <li>
                                                        <i class="icon-checkmark-circle text-success mr-2"></i>
                                                        START <span>${item['start_time']}</span> 
                                                        END <span>${item['end_time']}</span> 
                                                    </li>
                                                    `
                                                }) 
                                                console.log('res', response)
                                            }
                                        });
                                    }
                                    return json.map((item) => {
                                        return {
                                            day: item.day,
                                            employee: item.employee.emp_full_name,
                                            employee_id: item.employee.username
                                        }
                                    })
                                }
                            }
                        } );   
                        // } );	

                    document.getElementById('event-details-sidebar').style.display = 'flex';
                    }
                    // if (confirm('Are you sure you want to delete this event?')) {
                    //     arg.event.remove();
                    // }
                },
                editable: true,
                direction: document.dir == 'rtl' ? 'rtl' : 'ltr',
                dayMaxEvents: true // allow "more" link when too many events
            });

            // Init
            calendarSelectableInit.render();

            // Resize calendar when sidebar toggler is clicked
            $('.sidebar-control').on('click', function() {
                calendarSelectableInit.updateSize();
            });
        }
    };


    //
    // Return objects assigned to module
    //

    return {
        init: function() {
            _componentFullCalendarEvents();
            _componentFullCalendarSelectable();
        }
    }
}();


// Initialize module
// ------------------------------

document.addEventListener('DOMContentLoaded', function() {
    FullCalendarAdvanced.init();
});
