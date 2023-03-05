package main

import (
	"fmt"
	"strconv"
	"strings"
)

type pageInt struct {
	start int
	stop  int
}

func main() {
	var kk int
	fmt.Scanf("%d", &kk)

	for k := 0; k < kk; k++ {
		var pages int
		fmt.Scanf("%d", &pages)
		var printed string
		fmt.Scanf("%s\n", &printed)
		pi := []pageInt{}

		for _, interval := range strings.Split(printed, ",") {
			bounds := strings.Split(interval, "-")

			if len(bounds) == 1 {
				start, _ := strconv.Atoi(bounds[0])
				pi = append(pi, pageInt{start, start})
			} else {
				start, _ := strconv.Atoi(bounds[0])
				stop, _ := strconv.Atoi(bounds[1])
				pi = append(pi, pageInt{start, stop})
			}
		}

		toPrint := []string{}
		first := 0
		last := 0
		p := 0

	PAGES:
		for p = 1; p <= pages; p++ {
			for _, i := range pi {
				if i.start <= p && p <= i.stop {
					continue PAGES
				}
			}

			if last == 0 {
				last = p
				first = p
			} else if last+1 == p {
				last = p
			} else {
				var i string
				if first == last {
					i = fmt.Sprintf("%d", first)
				} else {
					i = fmt.Sprintf("%d-%d", first, last)
				}
				toPrint = append(toPrint, i)

				first = p
				last = p
			}
		}
		var i string
		if last == 0 && first == 0 {
			continue
		}

		if last == 0 || first == last {
			i = fmt.Sprintf("%d", first)
		} else {
			i = fmt.Sprintf("%d-%d", first, last)
		}

		toPrint = append(toPrint, i)
		fmt.Printf("%s\n", strings.Join(toPrint, ","))
	}
}