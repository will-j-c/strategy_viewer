import { LineChart, Line, XAxis, YAxis } from 'recharts';
import { PairsData } from '@/app/pairs/interfaces';

export default function PairsChart(props) {
    return (
        <LineChart width="100%" height="100%" responsive data={props.data}>
            <XAxis
                dataKey="time"
                type="category"
                angle={45}
                interval="preserveStartEnd"
                minTickGap={1}
                // dx={15}
                dy={80}
                // scale={"utc"}
            />
            <YAxis width="auto" />
            <Line dataKey="spread" dot={false} />
        </LineChart>
    );
}