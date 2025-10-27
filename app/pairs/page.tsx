"use client"
import { fetchFromApi } from "../helpers/helpers";
import { useState, useEffect } from "react";
import { PairsData } from "./interfaces";
import PairsChart from "../ui/charts/PairsChart";

export default function Pairs() {
  const [data, setData] = useState<PairsData[] | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      const data: PairsData[] = await fetchFromApi("http://127.0.0.1:5000/pairs/PF_XBTUSD/PF_DOTUSD/60/3.3/72/4/4");
      setData(data);
    }
    fetchData();
  }, [])

  return (
    (data !== null) ?
      (<PairsChart data={data}/>) : ("Loading")
  );
}