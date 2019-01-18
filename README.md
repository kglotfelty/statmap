# `statmap`

This little script is used to compute the mean|median energy 
of events based on how they have been spatially grouped via
the input map file.

So the basic idea is that a user creates a map (2D image) whose pixels
values identify spatial groups.  This could be the output of say
`dmnautilus` or some other binning algorithm (eg `contour_bin`).

The script identifies the events in each group, computes the 
specified statistic for the specified column, and then outputs 
an image with the stat value replacing the mapID value, eg
a median_energy map.

## Example

```bash
statmap acis_evt.fits[ccd_id=7,energy=500:2000] cbin.map mean_energy.map col=energy stat=mean 
```

## Install

This script requires CIAO be installed.


