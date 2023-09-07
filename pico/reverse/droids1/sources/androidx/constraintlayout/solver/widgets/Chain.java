package androidx.constraintlayout.solver.widgets;

import androidx.constraintlayout.solver.ArrayRow;
import androidx.constraintlayout.solver.LinearSystem;
import androidx.constraintlayout.solver.SolverVariable;
import androidx.constraintlayout.solver.widgets.ConstraintWidget;
import java.util.ArrayList;

/* loaded from: classes.dex */
class Chain {
    private static final boolean DEBUG = false;

    Chain() {
    }

    static void applyChainConstraints(ConstraintWidgetContainer constraintWidgetContainer, LinearSystem system, int orientation) {
        int offset;
        int chainsSize;
        ChainHead[] chainsArray;
        if (orientation == 0) {
            offset = 0;
            chainsSize = constraintWidgetContainer.mHorizontalChainsSize;
            chainsArray = constraintWidgetContainer.mHorizontalChainsArray;
        } else {
            offset = 2;
            chainsSize = constraintWidgetContainer.mVerticalChainsSize;
            chainsArray = constraintWidgetContainer.mVerticalChainsArray;
        }
        for (int i = 0; i < chainsSize; i++) {
            ChainHead first = chainsArray[i];
            first.define();
            if (constraintWidgetContainer.optimizeFor(4)) {
                if (!Optimizer.applyChainOptimized(constraintWidgetContainer, system, orientation, offset, first)) {
                    applyChainConstraints(constraintWidgetContainer, system, orientation, offset, first);
                }
            } else {
                applyChainConstraints(constraintWidgetContainer, system, orientation, offset, first);
            }
        }
    }

    /* JADX WARN: Removed duplicated region for block: B:296:0x064c  */
    /* JADX WARN: Removed duplicated region for block: B:297:0x0651  */
    /* JADX WARN: Removed duplicated region for block: B:300:0x0658  */
    /* JADX WARN: Removed duplicated region for block: B:301:0x065d  */
    /* JADX WARN: Removed duplicated region for block: B:303:0x0660  */
    /* JADX WARN: Removed duplicated region for block: B:308:0x0674  */
    /* JADX WARN: Removed duplicated region for block: B:310:0x0678  */
    /* JADX WARN: Removed duplicated region for block: B:311:0x0684  */
    /*
        Code decompiled incorrectly, please refer to instructions dump.
    */
    static void applyChainConstraints(ConstraintWidgetContainer container, LinearSystem system, int orientation, int offset, ChainHead chainHead) {
        boolean isChainSpread;
        boolean isChainSpreadInside;
        boolean isChainPacked;
        ConstraintWidget widget;
        ConstraintWidget widget2;
        ArrayList<ConstraintWidget> listMatchConstraints;
        ConstraintWidget widget3;
        ConstraintWidget previousMatchConstraintsWidget;
        SolverVariable beginTarget;
        SolverVariable endTarget;
        ConstraintAnchor end;
        ConstraintAnchor endTarget2;
        ConstraintAnchor end2;
        ConstraintWidget previousVisibleWidget;
        ConstraintWidget widget4;
        ConstraintWidget next;
        ConstraintWidget next2;
        ConstraintAnchor beginNextAnchor;
        SolverVariable beginNextTarget;
        SolverVariable beginNext;
        int strength;
        ConstraintWidget next3;
        SolverVariable beginTarget2;
        ConstraintAnchor beginNextAnchor2;
        SolverVariable beginNext2;
        SolverVariable beginNextTarget2;
        ConstraintWidget next4;
        ConstraintWidget previousVisibleWidget2;
        ConstraintWidget widget5;
        int nextMargin;
        int margin1;
        int margin2;
        int strength2;
        ConstraintAnchor begin;
        ConstraintAnchor end3;
        float bias;
        float totalWeights;
        ArrayList<ConstraintWidget> listMatchConstraints2;
        ConstraintWidget widget6;
        ConstraintWidget previousMatchConstraintsWidget2;
        ConstraintWidget firstMatchConstraintsWidget;
        int margin;
        int strength3;
        float totalWeights2;
        int strength4;
        ConstraintWidget next5;
        ConstraintWidget first = chainHead.mFirst;
        ConstraintWidget last = chainHead.mLast;
        ConstraintWidget firstVisibleWidget = chainHead.mFirstVisibleWidget;
        ConstraintWidget lastVisibleWidget = chainHead.mLastVisibleWidget;
        ConstraintWidget head = chainHead.mHead;
        float totalWeights3 = chainHead.mTotalWeight;
        ConstraintWidget firstMatchConstraintsWidget2 = chainHead.mFirstMatchConstraintWidget;
        ConstraintWidget previousMatchConstraintsWidget3 = chainHead.mLastMatchConstraintWidget;
        boolean isWrapContent = container.mListDimensionBehaviors[orientation] == ConstraintWidget.DimensionBehaviour.WRAP_CONTENT;
        if (orientation == 0) {
            boolean isChainSpread2 = head.mHorizontalChainStyle == 0;
            isChainSpread = isChainSpread2;
            boolean isChainSpreadInside2 = head.mHorizontalChainStyle == 1;
            isChainSpreadInside = isChainSpreadInside2;
            isChainPacked = head.mHorizontalChainStyle == 2;
            widget = first;
            widget2 = null;
        } else {
            boolean isChainSpread3 = head.mVerticalChainStyle == 0;
            isChainSpread = isChainSpread3;
            boolean isChainSpreadInside3 = head.mVerticalChainStyle == 1;
            isChainSpreadInside = isChainSpreadInside3;
            isChainPacked = head.mVerticalChainStyle == 2;
            widget = first;
            widget2 = null;
        }
        while (widget2 == null) {
            ConstraintAnchor begin2 = widget.mListAnchors[offset];
            int strength5 = 4;
            strength5 = (isWrapContent || isChainPacked) ? 1 : 1;
            int margin3 = begin2.getMargin();
            if (begin2.mTarget != null && widget != first) {
                margin = margin3 + begin2.mTarget.getMargin();
            } else {
                margin = margin3;
            }
            if (isChainPacked && widget != first && widget != firstVisibleWidget) {
                strength3 = 6;
            } else if (isChainSpread && isWrapContent) {
                strength3 = 4;
            } else {
                strength3 = strength5;
            }
            if (begin2.mTarget == null) {
                totalWeights2 = totalWeights3;
                strength4 = strength3;
            } else {
                if (widget == firstVisibleWidget) {
                    totalWeights2 = totalWeights3;
                    system.addGreaterThan(begin2.mSolverVariable, begin2.mTarget.mSolverVariable, margin, 5);
                } else {
                    totalWeights2 = totalWeights3;
                    system.addGreaterThan(begin2.mSolverVariable, begin2.mTarget.mSolverVariable, margin, 6);
                }
                strength4 = strength3;
                system.addEquality(begin2.mSolverVariable, begin2.mTarget.mSolverVariable, margin, strength4);
            }
            if (isWrapContent) {
                if (widget.getVisibility() != 8 && widget.mListDimensionBehaviors[orientation] == ConstraintWidget.DimensionBehaviour.MATCH_CONSTRAINT) {
                    system.addGreaterThan(widget.mListAnchors[offset + 1].mSolverVariable, widget.mListAnchors[offset].mSolverVariable, 0, 5);
                }
                system.addGreaterThan(widget.mListAnchors[offset].mSolverVariable, container.mListAnchors[offset].mSolverVariable, 0, 6);
            }
            ConstraintAnchor nextAnchor = widget.mListAnchors[offset + 1].mTarget;
            if (nextAnchor != null) {
                ConstraintWidget next6 = nextAnchor.mOwner;
                next5 = (next6.mListAnchors[offset].mTarget == null || next6.mListAnchors[offset].mTarget.mOwner != widget) ? null : next6;
            } else {
                next5 = null;
            }
            if (next5 != null) {
                widget = next5;
            } else {
                widget2 = 1;
            }
            totalWeights3 = totalWeights2;
        }
        float totalWeights4 = totalWeights3;
        if (lastVisibleWidget != null && last.mListAnchors[offset + 1].mTarget != null) {
            ConstraintAnchor end4 = lastVisibleWidget.mListAnchors[offset + 1];
            system.addLowerThan(end4.mSolverVariable, last.mListAnchors[offset + 1].mTarget.mSolverVariable, -end4.getMargin(), 5);
        }
        if (isWrapContent) {
            system.addGreaterThan(container.mListAnchors[offset + 1].mSolverVariable, last.mListAnchors[offset + 1].mSolverVariable, last.mListAnchors[offset + 1].getMargin(), 6);
        }
        ArrayList<ConstraintWidget> listMatchConstraints3 = chainHead.mWeightedMatchConstraintsWidgets;
        if (listMatchConstraints3 == null) {
            listMatchConstraints = listMatchConstraints3;
            widget3 = widget;
            previousMatchConstraintsWidget = previousMatchConstraintsWidget3;
        } else {
            int count = listMatchConstraints3.size();
            if (count > 1) {
                if (chainHead.mHasUndefinedWeights && !chainHead.mHasComplexMatchWeights) {
                    totalWeights = chainHead.mWidgetsMatchCount;
                } else {
                    totalWeights = totalWeights4;
                }
                ConstraintWidget lastMatch = null;
                int i = 0;
                float lastWeight = 0.0f;
                while (i < count) {
                    ConstraintWidget match = listMatchConstraints3.get(i);
                    int count2 = count;
                    float currentWeight = match.mWeight[orientation];
                    if (currentWeight >= 0.0f) {
                        listMatchConstraints2 = listMatchConstraints3;
                        widget6 = widget;
                        previousMatchConstraintsWidget2 = previousMatchConstraintsWidget3;
                    } else if (chainHead.mHasComplexMatchWeights) {
                        listMatchConstraints2 = listMatchConstraints3;
                        widget6 = widget;
                        previousMatchConstraintsWidget2 = previousMatchConstraintsWidget3;
                        system.addEquality(match.mListAnchors[offset + 1].mSolverVariable, match.mListAnchors[offset].mSolverVariable, 0, 4);
                        firstMatchConstraintsWidget = firstMatchConstraintsWidget2;
                        i++;
                        firstMatchConstraintsWidget2 = firstMatchConstraintsWidget;
                        count = count2;
                        listMatchConstraints3 = listMatchConstraints2;
                        widget = widget6;
                        previousMatchConstraintsWidget3 = previousMatchConstraintsWidget2;
                    } else {
                        listMatchConstraints2 = listMatchConstraints3;
                        widget6 = widget;
                        previousMatchConstraintsWidget2 = previousMatchConstraintsWidget3;
                        currentWeight = 1.0f;
                    }
                    if (currentWeight == 0.0f) {
                        firstMatchConstraintsWidget = firstMatchConstraintsWidget2;
                        system.addEquality(match.mListAnchors[offset + 1].mSolverVariable, match.mListAnchors[offset].mSolverVariable, 0, 6);
                    } else {
                        firstMatchConstraintsWidget = firstMatchConstraintsWidget2;
                        if (lastMatch != null) {
                            SolverVariable begin3 = lastMatch.mListAnchors[offset].mSolverVariable;
                            SolverVariable end5 = lastMatch.mListAnchors[offset + 1].mSolverVariable;
                            SolverVariable nextBegin = match.mListAnchors[offset].mSolverVariable;
                            SolverVariable nextEnd = match.mListAnchors[offset + 1].mSolverVariable;
                            ArrayRow row = system.createRow();
                            row.createRowEqualMatchDimensions(lastWeight, totalWeights, currentWeight, begin3, end5, nextBegin, nextEnd);
                            system.addConstraint(row);
                        }
                        lastWeight = currentWeight;
                        lastMatch = match;
                    }
                    i++;
                    firstMatchConstraintsWidget2 = firstMatchConstraintsWidget;
                    count = count2;
                    listMatchConstraints3 = listMatchConstraints2;
                    widget = widget6;
                    previousMatchConstraintsWidget3 = previousMatchConstraintsWidget2;
                }
                listMatchConstraints = listMatchConstraints3;
                widget3 = widget;
                previousMatchConstraintsWidget = previousMatchConstraintsWidget3;
            } else {
                listMatchConstraints = listMatchConstraints3;
                widget3 = widget;
                previousMatchConstraintsWidget = previousMatchConstraintsWidget3;
            }
        }
        if (firstVisibleWidget != null && (firstVisibleWidget == lastVisibleWidget || isChainPacked)) {
            ConstraintAnchor begin4 = first.mListAnchors[offset];
            ConstraintAnchor end6 = last.mListAnchors[offset + 1];
            SolverVariable beginTarget3 = first.mListAnchors[offset].mTarget != null ? first.mListAnchors[offset].mTarget.mSolverVariable : null;
            SolverVariable endTarget3 = last.mListAnchors[offset + 1].mTarget != null ? last.mListAnchors[offset + 1].mTarget.mSolverVariable : null;
            if (firstVisibleWidget != lastVisibleWidget) {
                begin = begin4;
                end3 = end6;
            } else {
                begin = firstVisibleWidget.mListAnchors[offset];
                end3 = firstVisibleWidget.mListAnchors[offset + 1];
            }
            if (beginTarget3 != null && endTarget3 != null) {
                if (orientation == 0) {
                    float bias2 = head.mHorizontalBiasPercent;
                    bias = bias2;
                } else {
                    float bias3 = head.mVerticalBiasPercent;
                    bias = bias3;
                }
                int beginMargin = begin.getMargin();
                int endMargin = end3.getMargin();
                system.addCentering(begin.mSolverVariable, beginTarget3, beginMargin, bias, endTarget3, end3.mSolverVariable, endMargin, 5);
            }
            if ((!isChainSpread || isChainSpreadInside) && firstVisibleWidget != null) {
                ConstraintAnchor begin5 = firstVisibleWidget.mListAnchors[offset];
                ConstraintAnchor end7 = lastVisibleWidget.mListAnchors[offset + 1];
                beginTarget = begin5.mTarget == null ? begin5.mTarget.mSolverVariable : null;
                SolverVariable endTarget4 = end7.mTarget == null ? end7.mTarget.mSolverVariable : null;
                if (last != lastVisibleWidget) {
                    endTarget = endTarget4;
                } else {
                    ConstraintAnchor realEnd = last.mListAnchors[offset + 1];
                    SolverVariable endTarget5 = realEnd.mTarget != null ? realEnd.mTarget.mSolverVariable : null;
                    endTarget = endTarget5;
                }
                if (firstVisibleWidget == lastVisibleWidget) {
                    end = end7;
                } else {
                    begin5 = firstVisibleWidget.mListAnchors[offset];
                    end = firstVisibleWidget.mListAnchors[offset + 1];
                }
                if (beginTarget == null && endTarget != null) {
                    int beginMargin2 = begin5.getMargin();
                    if (lastVisibleWidget == null) {
                        lastVisibleWidget = last;
                    }
                    int endMargin2 = lastVisibleWidget.mListAnchors[offset + 1].getMargin();
                    system.addCentering(begin5.mSolverVariable, beginTarget, beginMargin2, 0.5f, endTarget, end.mSolverVariable, endMargin2, 5);
                    return;
                }
            }
            return;
        }
        if (!isChainSpread || firstVisibleWidget == null) {
            int i2 = 8;
            if (isChainSpreadInside && firstVisibleWidget != null) {
                boolean applyFixedEquality = chainHead.mWidgetsMatchCount > 0 && chainHead.mWidgetsCount == chainHead.mWidgetsMatchCount;
                ConstraintWidget widget7 = firstVisibleWidget;
                ConstraintWidget previousVisibleWidget3 = firstVisibleWidget;
                while (widget7 != null) {
                    ConstraintWidget next7 = widget7.mNextChainWidget[orientation];
                    while (next7 != null && next7.getVisibility() == i2) {
                        next7 = next7.mNextChainWidget[orientation];
                    }
                    if (widget7 == firstVisibleWidget || widget7 == lastVisibleWidget || next7 == null) {
                        previousVisibleWidget = previousVisibleWidget3;
                        widget4 = widget7;
                        next = next7;
                    } else {
                        if (next7 != lastVisibleWidget) {
                            next2 = next7;
                        } else {
                            next2 = null;
                        }
                        ConstraintAnchor beginAnchor = widget7.mListAnchors[offset];
                        SolverVariable begin6 = beginAnchor.mSolverVariable;
                        if (beginAnchor.mTarget != null) {
                            SolverVariable solverVariable = beginAnchor.mTarget.mSolverVariable;
                        }
                        SolverVariable beginTarget4 = previousVisibleWidget3.mListAnchors[offset + 1].mSolverVariable;
                        SolverVariable beginNext3 = null;
                        int beginMargin3 = beginAnchor.getMargin();
                        int nextMargin2 = widget7.mListAnchors[offset + 1].getMargin();
                        if (next2 != null) {
                            ConstraintAnchor beginNextAnchor3 = next2.mListAnchors[offset];
                            SolverVariable beginNext4 = beginNextAnchor3.mSolverVariable;
                            beginNextTarget = beginNextAnchor3.mTarget != null ? beginNextAnchor3.mTarget.mSolverVariable : null;
                            beginNext = beginNext4;
                            beginNextAnchor = beginNextAnchor3;
                        } else {
                            ConstraintAnchor beginNextAnchor4 = widget7.mListAnchors[offset + 1].mTarget;
                            if (beginNextAnchor4 != null) {
                                beginNext3 = beginNextAnchor4.mSolverVariable;
                            }
                            beginNextAnchor = beginNextAnchor4;
                            beginNextTarget = widget7.mListAnchors[offset + 1].mSolverVariable;
                            beginNext = beginNext3;
                        }
                        if (beginNextAnchor != null) {
                            nextMargin2 += beginNextAnchor.getMargin();
                        }
                        if (previousVisibleWidget3 != null) {
                            beginMargin3 += previousVisibleWidget3.mListAnchors[offset + 1].getMargin();
                        }
                        if (!applyFixedEquality) {
                            strength = 4;
                        } else {
                            strength = 6;
                        }
                        if (begin6 == null || beginTarget4 == null || beginNext == null || beginNextTarget == null) {
                            next3 = next2;
                            previousVisibleWidget = previousVisibleWidget3;
                            widget4 = widget7;
                        } else {
                            next3 = next2;
                            previousVisibleWidget = previousVisibleWidget3;
                            widget4 = widget7;
                            system.addCentering(begin6, beginTarget4, beginMargin3, 0.5f, beginNext, beginNextTarget, nextMargin2, strength);
                        }
                        next = next3;
                    }
                    if (widget4.getVisibility() == 8) {
                        previousVisibleWidget3 = previousVisibleWidget;
                    } else {
                        previousVisibleWidget3 = widget4;
                    }
                    widget7 = next;
                    i2 = 8;
                }
                ConstraintAnchor begin7 = firstVisibleWidget.mListAnchors[offset];
                ConstraintAnchor beginTarget5 = first.mListAnchors[offset].mTarget;
                ConstraintAnchor end8 = lastVisibleWidget.mListAnchors[offset + 1];
                ConstraintAnchor endTarget6 = last.mListAnchors[offset + 1].mTarget;
                if (beginTarget5 == null) {
                    endTarget2 = endTarget6;
                    end2 = end8;
                } else if (firstVisibleWidget != lastVisibleWidget) {
                    system.addEquality(begin7.mSolverVariable, beginTarget5.mSolverVariable, begin7.getMargin(), 5);
                    endTarget2 = endTarget6;
                    end2 = end8;
                } else if (endTarget6 == null) {
                    endTarget2 = endTarget6;
                    end2 = end8;
                } else {
                    endTarget2 = endTarget6;
                    end2 = end8;
                    system.addCentering(begin7.mSolverVariable, beginTarget5.mSolverVariable, begin7.getMargin(), 0.5f, end8.mSolverVariable, endTarget6.mSolverVariable, end8.getMargin(), 5);
                }
                ConstraintAnchor endTarget7 = endTarget2;
                if (endTarget7 != null && firstVisibleWidget != lastVisibleWidget) {
                    ConstraintAnchor end9 = end2;
                    system.addEquality(end9.mSolverVariable, endTarget7.mSolverVariable, -end9.getMargin(), 5);
                }
            }
        } else {
            boolean applyFixedEquality2 = chainHead.mWidgetsMatchCount > 0 && chainHead.mWidgetsCount == chainHead.mWidgetsMatchCount;
            ConstraintWidget previousVisibleWidget4 = firstVisibleWidget;
            for (ConstraintWidget widget8 = firstVisibleWidget; widget8 != null; widget8 = next4) {
                ConstraintWidget next8 = widget8.mNextChainWidget[orientation];
                while (next8 != null && next8.getVisibility() == 8) {
                    next8 = next8.mNextChainWidget[orientation];
                }
                if (next8 != null || widget8 == lastVisibleWidget) {
                    ConstraintAnchor beginAnchor2 = widget8.mListAnchors[offset];
                    SolverVariable begin8 = beginAnchor2.mSolverVariable;
                    SolverVariable beginTarget6 = beginAnchor2.mTarget != null ? beginAnchor2.mTarget.mSolverVariable : null;
                    if (previousVisibleWidget4 != widget8) {
                        beginTarget2 = previousVisibleWidget4.mListAnchors[offset + 1].mSolverVariable;
                    } else if (widget8 == firstVisibleWidget && previousVisibleWidget4 == widget8) {
                        beginTarget2 = first.mListAnchors[offset].mTarget != null ? first.mListAnchors[offset].mTarget.mSolverVariable : null;
                    } else {
                        beginTarget2 = beginTarget6;
                    }
                    SolverVariable beginNext5 = null;
                    int beginMargin4 = beginAnchor2.getMargin();
                    int nextMargin3 = widget8.mListAnchors[offset + 1].getMargin();
                    if (next8 != null) {
                        ConstraintAnchor beginNextAnchor5 = next8.mListAnchors[offset];
                        SolverVariable beginNext6 = beginNextAnchor5.mSolverVariable;
                        SolverVariable beginNextTarget3 = widget8.mListAnchors[offset + 1].mSolverVariable;
                        beginNextAnchor2 = beginNextAnchor5;
                        beginNext2 = beginNext6;
                        beginNextTarget2 = beginNextTarget3;
                    } else {
                        ConstraintAnchor beginNextAnchor6 = last.mListAnchors[offset + 1].mTarget;
                        if (beginNextAnchor6 != null) {
                            beginNext5 = beginNextAnchor6.mSolverVariable;
                        }
                        SolverVariable beginNextTarget4 = widget8.mListAnchors[offset + 1].mSolverVariable;
                        beginNextAnchor2 = beginNextAnchor6;
                        beginNext2 = beginNext5;
                        beginNextTarget2 = beginNextTarget4;
                    }
                    if (beginNextAnchor2 != null) {
                        nextMargin3 += beginNextAnchor2.getMargin();
                    }
                    if (previousVisibleWidget4 != null) {
                        beginMargin4 += previousVisibleWidget4.mListAnchors[offset + 1].getMargin();
                    }
                    if (begin8 == null || beginTarget2 == null || beginNext2 == null || beginNextTarget2 == null) {
                        next4 = next8;
                        previousVisibleWidget2 = previousVisibleWidget4;
                        widget5 = widget8;
                        nextMargin = 8;
                    } else {
                        int margin12 = beginMargin4;
                        if (widget8 != firstVisibleWidget) {
                            margin1 = margin12;
                        } else {
                            int margin13 = firstVisibleWidget.mListAnchors[offset].getMargin();
                            margin1 = margin13;
                        }
                        int margin14 = nextMargin3;
                        if (widget8 != lastVisibleWidget) {
                            margin2 = margin14;
                        } else {
                            int margin22 = lastVisibleWidget.mListAnchors[offset + 1].getMargin();
                            margin2 = margin22;
                        }
                        if (!applyFixedEquality2) {
                            strength2 = 4;
                        } else {
                            strength2 = 6;
                        }
                        nextMargin = 8;
                        next4 = next8;
                        previousVisibleWidget2 = previousVisibleWidget4;
                        widget5 = widget8;
                        system.addCentering(begin8, beginTarget2, margin1, 0.5f, beginNext2, beginNextTarget2, margin2, strength2);
                    }
                } else {
                    next4 = next8;
                    previousVisibleWidget2 = previousVisibleWidget4;
                    widget5 = widget8;
                    nextMargin = 8;
                }
                if (widget5.getVisibility() == nextMargin) {
                    previousVisibleWidget4 = previousVisibleWidget2;
                } else {
                    previousVisibleWidget4 = widget5;
                }
            }
        }
        if (!isChainSpread) {
        }
        ConstraintAnchor begin52 = firstVisibleWidget.mListAnchors[offset];
        ConstraintAnchor end72 = lastVisibleWidget.mListAnchors[offset + 1];
        beginTarget = begin52.mTarget == null ? begin52.mTarget.mSolverVariable : null;
        if (end72.mTarget == null) {
        }
        if (last != lastVisibleWidget) {
        }
        if (firstVisibleWidget == lastVisibleWidget) {
        }
        if (beginTarget == null) {
        }
    }
}
