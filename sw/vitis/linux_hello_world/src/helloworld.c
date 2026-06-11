#include <stdio.h>
#include <systemd/sd-daemon.h>
#include <time.h>
#include <unistd.h>

int main()
{
    struct timespec now, next;
    int interval_sec = 10;

    sd_notify(0, "READY=1");

    clock_gettime(CLOCK_MONOTONIC, &next);
    next.tv_sec += interval_sec;

    while (1) {
        clock_gettime(CLOCK_MONOTONIC, &now);
        if (now.tv_sec > next.tv_sec || (now.tv_sec == next.tv_sec && now.tv_nsec >= next.tv_nsec)) {
            printf("10 second timer went off\r\n");
            next.tv_sec += interval_sec;
        }
        sleep(1);
        printf("Hello\r\n");
        sleep(1);
        printf("World!\r\n");
        /* If this were a Windows SCM service or a launchd service (macOS), you
         * could add a watchdog by creating a new thread that polls a global
         * atomic variable watchdog. If the main thread doesn't feed it from
         * its superloop on time, then the watchdog thread terminates/aborts the
         * entire process, which prompts SCM/launchd to restart the process after
         * a specified number of seconds.
         */
        sd_notify(0, "WATCHDOG=1");
    }
}
