"""
PineForge AI CLI — elite trading indicator analysis prompt generator.

Usage:
    python -m pineforge_ai.cli --symbol BTC/USDT --timeframes 1h,4h,1d --days 60
    python -m pineforge_ai.cli --symbol BTC/USDT --mode mindset --timeframes 15m,1h,4h --days 7
    python -m pineforge_ai.cli --symbol BTC/USDT --indicators wavetrend,smc --no-context
    python -m pineforge_ai.cli --symbol BTC/USDT --send-to-ai --api-key $KEY
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone

import click

from pineforge_ai.config import (
    ALL_INDICATORS,
    DEFAULT_DAYS,
    DEFAULT_EXCHANGE,
    DEFAULT_OUTPUT_DIR,
    DEFAULT_TIMEFRAMES,
    VALID_TIMEFRAMES,
)


@click.command()
@click.option("--symbol",     required=True,  help="BTC/USDT, AAPL, ^FTSE, EURUSD=X")
@click.option("--indicators", default="all",  show_default=True,
              help=f"Comma list or 'all'. Available: {', '.join(ALL_INDICATORS)}")
@click.option("--timeframes", default=",".join(DEFAULT_TIMEFRAMES), show_default=True)
@click.option("--days",       default=DEFAULT_DAYS, show_default=True, type=int)
@click.option("--source",     default="auto", type=click.Choice(["auto", "yfinance", "ccxt"]))
@click.option("--exchange",   default=DEFAULT_EXCHANGE, show_default=True)
@click.option("--output",     default=DEFAULT_OUTPUT_DIR, show_default=True)
@click.option("--no-save",    is_flag=True, default=False, help="Print to stdout instead of saving")
@click.option("--no-context", is_flag=True, default=False, help="Skip correlations + volatility context")
@click.option("--send-to-ai", is_flag=True, default=False, help="Call Anthropic API after building prompt")
@click.option("--api-key",    default=None, help="Anthropic API key (or env ANTHROPIC_API_KEY)")
@click.option("--model",      default="claude-opus-4-7", show_default=True)
@click.option("--mode",       default="signal", show_default=True,
              type=click.Choice(["signal", "mindset"]),
              help="'signal': JSON signal analysis. 'mindset': Pre-NY Protocol checklist.")
def main(symbol, indicators, timeframes, days, source, exchange, output,
         no_save, no_context, send_to_ai, api_key, model, mode):
    dt_utc = datetime.now(tz=timezone.utc)

    tf_list = [t.strip().lower() for t in timeframes.split(",") if t.strip()]
    bad = [t for t in tf_list if t not in VALID_TIMEFRAMES]
    if bad:
        click.echo(f"ERROR: invalid TFs: {bad}", err=True); sys.exit(1)

    if indicators.lower() == "all":
        ind_list = ALL_INDICATORS
    else:
        ind_list = [i.strip().lower() for i in indicators.split(",") if i.strip()]
        bad_inds = [i for i in ind_list if i not in ALL_INDICATORS]
        if bad_inds:
            click.echo(f"ERROR: bad indicators: {bad_inds}. Valid: {ALL_INDICATORS}", err=True)
            sys.exit(1)

    click.echo(f"\n{'═'*70}")
    click.echo(f"  PINEFORGE AI v3")
    click.echo(f"  Symbol     : {symbol}")
    click.echo(f"  Mode       : {mode.upper()}")
    click.echo(f"  Indicators : {', '.join(ind_list)}")
    click.echo(f"  Timeframes : {', '.join(tf_list)}")
    click.echo(f"  Days       : {days}")
    click.echo(f"  Context    : {'OFF' if no_context else 'ON'}")
    click.echo(f"  Send to AI : {'YES' if send_to_ai else 'NO'}")
    click.echo(f"{'═'*70}\n")

    # ── Fetch ────────────────────────────────────────────────────────────────
    from pineforge_ai.data.fetcher import detect_source, fetch_multi_timeframe
    actual_source = source if source != "auto" else detect_source(symbol)
    click.echo(f"[1/4] Descargando OHLCV ({actual_source.upper()})...")
    try:
        dfs = fetch_multi_timeframe(symbol=symbol, timeframes=tf_list, days=days,
                                     source=actual_source, exchange=exchange)
    except Exception as e:
        click.echo(f"ERROR fetch: {e}", err=True); sys.exit(1)
    if not dfs:
        click.echo("ERROR: empty dfs", err=True); sys.exit(1)

    candle_counts = {tf: len(df) for tf, df in dfs.items()}

    # ── Indicators ───────────────────────────────────────────────────────────
    click.echo(f"[2/4] Calculando indicadores...")
    summaries: dict[str, dict | None] = {
        "wt": None, "lux": None, "smc": None,
        "tq": None, "it": None, "ict": None, "tl": None,
    }

    if "wavetrend" in ind_list:
        try:
            from pineforge_ai.indicators.wavetrend import wavetrend_all_timeframes, wavetrend_summary
            summaries["wt"] = wavetrend_summary(wavetrend_all_timeframes(dfs))
            click.echo(f"      WaveTrend OK")
        except Exception as e:
            click.echo(f"      WaveTrend FAIL: {e}")

    if "luxalgo" in ind_list:
        try:
            from pineforge_ai.indicators.luxalgo_amo import adaptive_momentum_all_timeframes, luxalgo_summary
            summaries["lux"] = luxalgo_summary(adaptive_momentum_all_timeframes(dfs))
            click.echo(f"      LuxAlgo AMO OK")
        except Exception as e:
            click.echo(f"      LuxAlgo FAIL: {e}")

    if "smc" in ind_list:
        try:
            from pineforge_ai.indicators.smc_buda import smc_all_timeframes, smc_summary
            summaries["smc"] = smc_summary(smc_all_timeframes(dfs))
            click.echo(f"      SMC Buda OK")
        except Exception as e:
            click.echo(f"      SMC FAIL: {e}")

    if "wae" in ind_list:
        try:
            from pineforge_ai.indicators.wae import trend_quality_all_timeframes, trend_quality_summary
            summaries["tq"] = trend_quality_summary(trend_quality_all_timeframes(dfs))
            click.echo(f"      WAE+Chop OK")
        except Exception as e:
            click.echo(f"      WAE FAIL: {e}")

    if "itrend" in ind_list:
        try:
            from pineforge_ai.indicators.itrend import itrend_all_timeframes, itrend_summary
            summaries["it"] = itrend_summary(itrend_all_timeframes(dfs))
            click.echo(f"      Ehlers iTrend OK")
        except Exception as e:
            click.echo(f"      iTrend FAIL: {e}")

    if "ict" in ind_list:
        try:
            from pineforge_ai.indicators.ict_concepts import ict_all_timeframes, ict_summary
            summaries["ict"] = ict_summary(ict_all_timeframes(dfs))
            click.echo(f"      ICT Concepts OK")
        except Exception as e:
            click.echo(f"      ICT FAIL: {e}")

    if "trendlines" in ind_list:
        try:
            from pineforge_ai.indicators.trendlines import trendlines_all_timeframes, trendlines_summary
            summaries["tl"] = trendlines_summary(trendlines_all_timeframes(dfs))
            click.echo(f"      Trendlines OK")
        except Exception as e:
            click.echo(f"      Trendlines FAIL: {e}")

    # ── Context ──────────────────────────────────────────────────────────────
    correlations = None
    volatility = None
    if not no_context:
        click.echo(f"[3/4] Contexto de mercado...")
        try:
            from pineforge_ai.context.correlations import fetch_correlations
            correlations = fetch_correlations(skip_btc_for=symbol)
            click.echo(f"      Correlations OK")
        except Exception as e:
            click.echo(f"      Correlations FAIL: {e}")
        try:
            from pineforge_ai.context.volatility import volatility_all_timeframes
            volatility = volatility_all_timeframes(dfs)
            click.echo(f"      Volatility OK")
        except Exception as e:
            click.echo(f"      Volatility FAIL: {e}")
    else:
        click.echo(f"[3/4] Contexto OFF")

    # ── USDT.D dominance (always attempted, graceful if daemon not running) ──
    usdt_data = None
    try:
        from pineforge_ai.usdt_dominance.reader import build_usdt_summary
        usdt_data = build_usdt_summary()
        if usdt_data.get("available"):
            click.echo(f"      USDT.D OK ({usdt_data['current']:.4f}%)")
        else:
            click.echo(f"      USDT.D: daemon not running (start: python -m pineforge_ai.usdt_dominance.daemon)")
    except Exception as e:
        click.echo(f"      USDT.D FAIL: {e}")

    # ── Build + save ─────────────────────────────────────────────────────────
    click.echo(f"[4/4] Ensamblando prompt ({mode.upper()})...")
    from pineforge_ai.prompt_builder import build_prompt, save_prompt, send_to_ai as send_fn

    prompt = build_prompt(
        symbol=symbol, dfs=dfs, timeframes=tf_list,
        wt_summary=summaries["wt"], lux_summary=summaries["lux"],
        smc_sum=summaries["smc"], tq_summary=summaries["tq"],
        cc_summary=None,
        ict_sum=summaries["ict"],
        tl_summary=summaries["tl"],
        it_summary=summaries["it"],
        correlations=correlations, volatility=volatility,
        usdt_data=usdt_data,
        source=actual_source, exchange=exchange,
        candle_counts=candle_counts, dt_utc=dt_utc,
        mode=mode,
    )

    if no_save:
        click.echo(prompt)
    else:
        try:
            fp = save_prompt(prompt, symbol=symbol, output_dir=output, dt_utc=dt_utc)
            click.echo(f"\n{'═'*70}\n  PROMPT GUARDADO\n  {fp}\n{'═'*70}")
        except Exception as e:
            click.echo(f"ERROR save: {e}", err=True); click.echo(prompt)

    # ── Optional API call ────────────────────────────────────────────────────
    if send_to_ai:
        click.echo(f"\nLlamando a Anthropic ({model}) — modo {mode.upper()}...")
        try:
            data = send_fn(prompt, api_key=api_key, model=model, mode=mode)
            json_path = (
                fp.replace(".txt", "_ai.json") if not no_save else
                f"./pineforge_ai_response_{dt_utc.strftime('%Y%m%d_%H%M')}.json"
            )
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            click.echo(f"  AI Response: {json_path}")
            usage = data.get("_usage", {})
            if usage:
                click.echo(f"  Tokens: in={usage.get('input_tokens')} out={usage.get('output_tokens')} "
                           f"cache_create={usage.get('cache_creation_input_tokens')} "
                           f"cache_read={usage.get('cache_read_input_tokens')}")
        except Exception as e:
            click.echo(f"AI call failed: {e}", err=True)


if __name__ == "__main__":
    main()
