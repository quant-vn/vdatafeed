""" Model for SSI datafeed """
from typing import Optional
from ..utils import BaseModel, Field, AliasChoices


class SecuritiesInfo(BaseModel):
    """
    Model class representing securities information.
    Attributes:
        instrument (Optional[str]): The instrument or symbol of the security.
        instrument_name (Optional[str]): The name of the instrument or symbol.
        securities_type (Optional[str]): The type of the security.
        exchange (Optional[str]): The exchange where the security is traded.
        issuer (Optional[str]): The issuer of the security.
        lot_size (Optional[str]): The lot size of the security.
        maturity_date (Optional[str]): The maturity date of the security.
        last_trading_date (Optional[str]): The last trading date of the security.
        contract_multiplier (Optional[str]): The contract multiplier of the security.
        underlying (Optional[str]): The underlying asset of the security.
        put_or_call (Optional[str]): The type of option (put or call) for the security.
        exercise_price (Optional[str]): The exercise price of the security.
        exercise_style (Optional[str]): The exercise style of the security.
        exercise_ratio (Optional[str]): The exercise ratio of the security.
        listed_share (Optional[str]): The listed share of the security.
        tick_price_1 (Optional[str]): The tick price 1 of the security.
        tick_increment_1 (Optional[str]): The tick increment 1 of the security.
        tick_price_2 (Optional[str]): The tick price 2 of the security.
        tick_increment_2 (Optional[str]): The tick increment 2 of the security.
        tick_price_3 (Optional[str]): The tick price 3 of the security.
        tick_increment_3 (Optional[str]): The tick increment 3 of the security.
    """
    instrument: Optional[str] = Field(validation_alias=AliasChoices('instrument', 'Symbol'))
    instrument_name: Optional[str] = Field(
        validation_alias=AliasChoices('instrument_name', 'SymbolName')
    )
    securities_type: Optional[str] = Field(
        validation_alias=AliasChoices('securities_type', 'SecType')
    )
    exchange: Optional[str] = Field(validation_alias=AliasChoices('exchange', 'Exchange'))
    issuer: Optional[str] = Field(validation_alias=AliasChoices('issuer', 'Issuer'))
    lot_size: Optional[str] = Field(validation_alias=AliasChoices('lot_size', 'LotSize'))
    maturity_date: Optional[str] = Field(
        validation_alias=AliasChoices('maturity_date', 'MaturityDate')
    )
    last_trading_date: Optional[str] = Field(
        validation_alias=AliasChoices('last_trading_date', 'LastTradingDate')
    )
    contract_multiplier: Optional[str] = Field(
        validation_alias=AliasChoices('contract_multiplier', 'ContractMultiplier')
    )
    underlying: Optional[str] = Field(validation_alias=AliasChoices('underlying', 'Underlying'))
    put_or_call: Optional[str] = Field(validation_alias=AliasChoices('put_or_call', 'PutOrCall'))
    exercise_price: Optional[str] = Field(
        validation_alias=AliasChoices('exercise_price', 'ExercisePrice')
    )
    exercise_style: Optional[str] = Field(
        validation_alias=AliasChoices('exercise_style', 'ExerciseStyle')
    )
    exercise_ratio: Optional[str] = Field(
        validation_alias=AliasChoices('exercise_ratio', 'ExcerciseRatio')
    )
    listed_share: Optional[str] = Field(
        validation_alias=AliasChoices('listed_share', 'ListedShare')
    )
    tick_price_1: Optional[str] = Field(validation_alias=AliasChoices('tick_price_1', 'TickPrice1'))
    tick_increment_1: Optional[str] = Field(
        validation_alias=AliasChoices('tick_increment_1', 'TickIncrement1')
    )
    tick_price_2: Optional[str] = Field(validation_alias=AliasChoices('tick_price_2', 'TickPrice2'))
    tick_increment_2: Optional[str] = Field(
        validation_alias=AliasChoices('tick_increment_2', 'TickIncrement2')
    )
    tick_price_3: Optional[str] = Field(validation_alias=AliasChoices('tick_price_3', 'TickPrice3'))
    tick_increment_3: Optional[str] = Field(
        validation_alias=AliasChoices('tick_increment_3', 'TickIncrement3')
    )


class IndexInfo(BaseModel):
    """
    Model class representing index information.
    Attributes:
        index_code (Optional[str]): The code of the index.
        exchange (Optional[str]): The exchange where the index is traded.
    """
    index_code: Optional[str] = Field(validation_alias=AliasChoices('index_code', 'IndexCode'))
    exchange: Optional[str] = Field(validation_alias=AliasChoices('exchange', 'Exchange'))


class InstrumentInfo(BaseModel):
    """
    Model class representing instrument information.
    Attributes:
        instrument (Optional[str]): The instrument symbol.
        trading_date (Optional[str]): The trading date.
        price_change (Optional[str]): The price change.
        per_price_change (Optional[str]): The percentage price change.
        ceiling (Optional[str]): The ceiling price.
        floor (Optional[str]): The floor price.
        ref (Optional[str]): The reference price.
        open (Optional[str]): The opening price.
        high (Optional[str]): The highest price.
        low (Optional[str]): The lowest price.
        close (Optional[str]): The closing price.
        avg_price (Optional[str]): The average price.
        close_adj (Optional[str]): The adjusted closing price.
        total_vol (Optional[str]): The total matched volume.
        total_val (Optional[str]): The total matched value.
        total_deal_val (Optional[str]): The total deal value.
        total_deal_vol (Optional[str]): The total deal volume.
        foreign_current_room (Optional[str]): The foreign current room.
        total_foreign_buy_vol (Optional[str]): The total foreign buy volume.
        total_foreign_buy_val (Optional[str]): The total foreign buy value.
        total_foreign_sell_val (Optional[str]): The total foreign sell value.
        total_foreign_sell_vol (Optional[str]): The total foreign sell volume.
        total_buy_trade (Optional[str]): The total buy trade.
        total_buy_trade_vol (Optional[str]): The total buy trade volume.
        total_sell_trade (Optional[str]): The total sell trade.
        total_sell_trade_vol (Optional[str]): The total sell trade volume.
        net_buy_sell_vol (Optional[str]): The net buy sell volume.
        net_buy_sell_val (Optional[str]): The net buy sell value.
        total_trade_vol (Optional[str]): The total traded volume.
        total_trade_val (Optional[str]): The total traded value.
    """
    instrument: Optional[str] = Field(validation_alias=AliasChoices('instrument', 'Symbol'))
    trading_date: Optional[str] = Field(
        validation_alias=AliasChoices('trading_date', 'TradingDate')
    )
    price_change: Optional[str] = Field(
        validation_alias=AliasChoices('price_change', 'PriceChange')
    )
    per_price_change: Optional[str] = Field(
        validation_alias=AliasChoices('per_price_change', 'PerPriceChange')
    )
    ceiling: Optional[str] = Field(validation_alias=AliasChoices('ceiling', 'CeilingPrice'))
    floor: Optional[str] = Field(validation_alias=AliasChoices('floor', 'FloorPrice'))
    ref: Optional[str] = Field(validation_alias=AliasChoices('ref', 'RefPrice'))
    open: Optional[str] = Field(validation_alias=AliasChoices('open', 'OpenPrice'))
    high: Optional[str] = Field(validation_alias=AliasChoices('high', 'HighestPrice'))
    low: Optional[str] = Field(validation_alias=AliasChoices('low', 'LowestPrice'))
    close: Optional[str] = Field(validation_alias=AliasChoices('close', 'ClosePrice'))
    avg_price: Optional[str] = Field(validation_alias=AliasChoices('avg_price', 'AveragePrice'))
    close_adj: Optional[str] = Field(
        validation_alias=AliasChoices('close_adj', 'ClosePriceAdjusted')
    )
    total_vol: Optional[str] = Field(validation_alias=AliasChoices('total_vol', 'TotalMatchVol'))
    total_val: Optional[str] = Field(validation_alias=AliasChoices('total_val', 'TotalMatchVal'))
    total_deal_val: Optional[str] = Field(
        validation_alias=AliasChoices('total_deal_val', 'TotalDealVal')
    )
    total_deal_vol: Optional[str] = Field(
        validation_alias=AliasChoices('total_deal_vol', 'TotalDealVol')
    )
    foreign_current_room: Optional[str] = Field(
        validation_alias=AliasChoices('foreign_current_room', 'ForeignCurrentRoom')
    )
    total_foreign_buy_vol: Optional[str] = Field(
        validation_alias=AliasChoices('total_foreign_buy_vol', 'ForeignBuyVolTotal')
    )
    total_foreign_buy_val: Optional[str] = Field(
        validation_alias=AliasChoices('total_foreign_buy_val', 'ForeignBuyValTotal')
    )
    total_foreign_sell_val: Optional[str] = Field(
        validation_alias=AliasChoices('total_foreign_sell_val', 'ForeignSellValTotal')
    )
    total_foreign_sell_vol: Optional[str] = Field(
        validation_alias=AliasChoices('total_foreign_sell_vol', 'ForeignSellVolTotal')
    )
    total_buy_trade: Optional[str] = Field(
        validation_alias=AliasChoices('total_buy_trade', 'TotalBuyTrade')
    )
    total_buy_trade_vol: Optional[str] = Field(
        validation_alias=AliasChoices('total_buy_trade_vol', 'TotalBuyTradeVol')
    )
    total_sell_trade: Optional[str] = Field(
        validation_alias=AliasChoices('total_sell_trade', 'TotalSellTrade')
    )
    total_sell_trade_vol: Optional[str] = Field(
        validation_alias=AliasChoices('total_sell_trade_vol', 'TotalSellTradeVol')
    )
    net_buy_sell_vol: Optional[str] = Field(
        validation_alias=AliasChoices('net_buy_sell_vol', 'NetBuySellVol')
    )
    net_buy_sell_val: Optional[str] = Field(
        validation_alias=AliasChoices('net_buy_sell_val', 'NetBuySellVal')
    )
    total_trade_vol: Optional[str] = Field(
        validation_alias=AliasChoices('total_trade_vol', 'TotalTradedVol')
    )
    total_trade_val: Optional[str] = Field(
        validation_alias=AliasChoices('total_trade_val', 'TotalTradedValue')
    )


class IndicesInfo(BaseModel):
    """
    Represents information about indices.
    Attributes:
        index (Optional[str]): The index ID.
        trading_date (Optional[str]): The trading date.
        type (Optional[str]): The type of index.
        name (Optional[str]): The name of the index.
        session (Optional[str]): The trading session.
        value (Optional[str]): The value of the index.
        change (Optional[str]): The change in the index.
        ratio_change (Optional[str]): The ratio change in the index.
        total_trade (Optional[str]): The total number of trades.
        total_match_vol (Optional[str]): The total matched volume.
        total_match_val (Optional[str]): The total matched value.
        advances (Optional[str]): The number of advances.
        no_changes (Optional[str]): The number of no changes.
        declines (Optional[str]): The number of declines.
        ceiling (Optional[str]): The number of ceilings.
        floor (Optional[str]): The number of floors.
        total_deal_vol (Optional[str]): The total deal volume.
        total_deal_val (Optional[str]): The total deal value.
        total_vol (Optional[str]): The total volume.
        total_val (Optional[str]): The total value.
    """
    index: Optional[str] = Field(validation_alias=AliasChoices('index', 'IndexId'))
    trading_date: Optional[str] = Field(
        validation_alias=AliasChoices('trading_date', 'TradingDate')
    )
    type: Optional[str] = Field(validation_alias=AliasChoices('type', 'TypeIndex'))
    name: Optional[str] = Field(validation_alias=AliasChoices('name', 'IndexName'))
    session: Optional[str] = Field(validation_alias=AliasChoices('session', 'TradingSession'))
    value: Optional[str] = Field(validation_alias=AliasChoices('value', 'IndexValue'))
    change: Optional[str] = Field(validation_alias=AliasChoices('change', 'Change'))
    ratio_change: Optional[str] = Field(
        validation_alias=AliasChoices('ratio_change', 'RatioChange')
    )
    total_trade: Optional[str] = Field(validation_alias=AliasChoices('total_trade', 'TotalTrade'))
    total_match_vol: Optional[str] = Field(
        validation_alias=AliasChoices('total_match_vol', 'TotalMatchVol')
    )
    total_match_val: Optional[str] = Field(
        validation_alias=AliasChoices('total_match_val', 'TotalMatchVal')
    )
    advances: Optional[str] = Field(validation_alias=AliasChoices('advances', 'Advances'))
    no_changes: Optional[str] = Field(validation_alias=AliasChoices('no_changes', 'NoChanges'))
    declines: Optional[str] = Field(validation_alias=AliasChoices('declines', 'Declines'))
    ceiling: Optional[str] = Field(validation_alias=AliasChoices('ceiling', 'Ceilings'))
    floor: Optional[str] = Field(validation_alias=AliasChoices('floor', 'Floors'))
    total_deal_vol: Optional[str] = Field(
        validation_alias=AliasChoices('total_deal_vol', 'TotalDealVol')
    )
    total_deal_val: Optional[str] = Field(
        validation_alias=AliasChoices('total_deal_val', 'TotalDealVal')
    )
    total_vol: Optional[str] = Field(validation_alias=AliasChoices('total_vol', 'TotalVol'))
    total_val: Optional[str] = Field(validation_alias=AliasChoices('total_val', 'TotalVal'))


class EndOfDayOHLC(BaseModel):
    """
    Represents the end-of-day OHLC (Open, High, Low, Close) data for a financial instrument.
    Attributes:
        instrument (Optional[str]): The symbol or identifier of the instrument.
        exchange (Optional[str]): The market or exchange where the instrument is traded.
        trading_date (Optional[str]): The date of the trading session.
        open (Optional[str]): The opening price of the instrument.
        high (Optional[str]): The highest price reached during the trading session.
        low (Optional[str]): The lowest price reached during the trading session.
        close (Optional[str]): The closing price of the instrument.
        vol (Optional[str]): The trading volume of the instrument.
        val (Optional[str]): The trading value of the instrument.
    """
    instrument: Optional[str] = Field(validation_alias=AliasChoices('instrument', 'Symbol'))
    exchange: Optional[str] = Field(validation_alias=AliasChoices('exchange', 'Market'))
    trading_date: Optional[str] = Field(
        validation_alias=AliasChoices('trading_date', 'TradingDate')
    )
    open: Optional[str] = Field(validation_alias=AliasChoices('open', 'Open'))
    high: Optional[str] = Field(validation_alias=AliasChoices('high', 'High'))
    low: Optional[str] = Field(validation_alias=AliasChoices('low', 'Low'))
    close: Optional[str] = Field(validation_alias=AliasChoices('close', 'Close'))
    vol: Optional[str] = Field(validation_alias=AliasChoices('vol', 'Volume'))
    val: Optional[str] = Field(validation_alias=AliasChoices('val', 'Value'))


class IntradayOHLC(BaseModel):
    instrument: Optional[str] = Field(validation_alias=AliasChoices('instrument', 'Symbol'))
    trading_date: Optional[str] = Field(
        validation_alias=AliasChoices('trading_date', 'TradingDate')
    )
    trading_time: Optional[str] = Field(validation_alias=AliasChoices('trading_time', 'Time'))
    open: Optional[str] = Field(validation_alias=AliasChoices('open', 'Open'))
    high: Optional[str] = Field(validation_alias=AliasChoices('high', 'High'))
    low: Optional[str] = Field(validation_alias=AliasChoices('low', 'Low'))
    close: Optional[str] = Field(validation_alias=AliasChoices('close', 'Close'))
    vol: Optional[str] = Field(validation_alias=AliasChoices('vol', 'Volume'))
    val: Optional[str] = Field(validation_alias=AliasChoices('val', 'Value'))
