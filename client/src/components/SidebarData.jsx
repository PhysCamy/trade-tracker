import React from 'react';
import "../App.css"
import BookIcon from '@mui/icons-material/Book';
import HandshakeIcon from '@mui/icons-material/Handshake';
import InventoryIcon from '@mui/icons-material/Inventory';
import ShowChartIcon from '@mui/icons-material/ShowChart';
import CandlestickChartIcon from '@mui/icons-material/CandlestickChart';

export const SidebarData = [
    {
        title: "Portfolios",
        icon: <BookIcon />,
        link: "/portfolios"
    },
    {
        title: "Transactions",
        icon: <HandshakeIcon />,
        link: "/transactions"
    },
    {
        title: "Holdings",
        icon: <InventoryIcon />,
        link: "/holdings"
    },
    {
        title: "Valuations",
        icon: <ShowChartIcon />,
        link: "/valuations"
    },
    {
        title: "Market Data",
        icon: <CandlestickChartIcon />,
        link: "/marketdata"
    }
];