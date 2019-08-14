#!/usr/bin/env sh

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Run the bar on each monitor
if type "xrandr"; then
  for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
    POLY_MONITOR=$m polybar --reload top  &
  done
else
  polybar --reload example &
fi

echo "Bars launched..."
