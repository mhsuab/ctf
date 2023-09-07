package androidx.constraintlayout.solver.widgets;

import androidx.constraintlayout.solver.LinearSystem;
import androidx.constraintlayout.solver.Metrics;
import androidx.constraintlayout.solver.widgets.ConstraintAnchor;
import androidx.constraintlayout.solver.widgets.ConstraintWidget;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/* loaded from: classes.dex */
public class ConstraintWidgetContainer extends WidgetContainer {
    private static final boolean DEBUG = false;
    static final boolean DEBUG_GRAPH = false;
    private static final boolean DEBUG_LAYOUT = false;
    private static final int MAX_ITERATIONS = 8;
    private static final boolean USE_SNAPSHOT = true;
    int mDebugSolverPassCount;
    public boolean mGroupsWrapOptimized;
    private boolean mHeightMeasuredTooSmall;
    ChainHead[] mHorizontalChainsArray;
    int mHorizontalChainsSize;
    public boolean mHorizontalWrapOptimized;
    private boolean mIsRtl;
    private int mOptimizationLevel;
    int mPaddingBottom;
    int mPaddingLeft;
    int mPaddingRight;
    int mPaddingTop;
    public boolean mSkipSolver;
    private Snapshot mSnapshot;
    protected LinearSystem mSystem;
    ChainHead[] mVerticalChainsArray;
    int mVerticalChainsSize;
    public boolean mVerticalWrapOptimized;
    public List<ConstraintWidgetGroup> mWidgetGroups;
    private boolean mWidthMeasuredTooSmall;
    public int mWrapFixedHeight;
    public int mWrapFixedWidth;

    public void fillMetrics(Metrics metrics) {
        this.mSystem.fillMetrics(metrics);
    }

    public ConstraintWidgetContainer() {
        this.mIsRtl = false;
        this.mSystem = new LinearSystem();
        this.mHorizontalChainsSize = 0;
        this.mVerticalChainsSize = 0;
        this.mVerticalChainsArray = new ChainHead[4];
        this.mHorizontalChainsArray = new ChainHead[4];
        this.mWidgetGroups = new ArrayList();
        this.mGroupsWrapOptimized = false;
        this.mHorizontalWrapOptimized = false;
        this.mVerticalWrapOptimized = false;
        this.mWrapFixedWidth = 0;
        this.mWrapFixedHeight = 0;
        this.mOptimizationLevel = 7;
        this.mSkipSolver = false;
        this.mWidthMeasuredTooSmall = false;
        this.mHeightMeasuredTooSmall = false;
        this.mDebugSolverPassCount = 0;
    }

    public ConstraintWidgetContainer(int x, int y, int width, int height) {
        super(x, y, width, height);
        this.mIsRtl = false;
        this.mSystem = new LinearSystem();
        this.mHorizontalChainsSize = 0;
        this.mVerticalChainsSize = 0;
        this.mVerticalChainsArray = new ChainHead[4];
        this.mHorizontalChainsArray = new ChainHead[4];
        this.mWidgetGroups = new ArrayList();
        this.mGroupsWrapOptimized = false;
        this.mHorizontalWrapOptimized = false;
        this.mVerticalWrapOptimized = false;
        this.mWrapFixedWidth = 0;
        this.mWrapFixedHeight = 0;
        this.mOptimizationLevel = 7;
        this.mSkipSolver = false;
        this.mWidthMeasuredTooSmall = false;
        this.mHeightMeasuredTooSmall = false;
        this.mDebugSolverPassCount = 0;
    }

    public ConstraintWidgetContainer(int width, int height) {
        super(width, height);
        this.mIsRtl = false;
        this.mSystem = new LinearSystem();
        this.mHorizontalChainsSize = 0;
        this.mVerticalChainsSize = 0;
        this.mVerticalChainsArray = new ChainHead[4];
        this.mHorizontalChainsArray = new ChainHead[4];
        this.mWidgetGroups = new ArrayList();
        this.mGroupsWrapOptimized = false;
        this.mHorizontalWrapOptimized = false;
        this.mVerticalWrapOptimized = false;
        this.mWrapFixedWidth = 0;
        this.mWrapFixedHeight = 0;
        this.mOptimizationLevel = 7;
        this.mSkipSolver = false;
        this.mWidthMeasuredTooSmall = false;
        this.mHeightMeasuredTooSmall = false;
        this.mDebugSolverPassCount = 0;
    }

    public void setOptimizationLevel(int value) {
        this.mOptimizationLevel = value;
    }

    public int getOptimizationLevel() {
        return this.mOptimizationLevel;
    }

    public boolean optimizeFor(int feature) {
        if ((this.mOptimizationLevel & feature) == feature) {
            return USE_SNAPSHOT;
        }
        return false;
    }

    @Override // androidx.constraintlayout.solver.widgets.ConstraintWidget
    public String getType() {
        return "ConstraintLayout";
    }

    @Override // androidx.constraintlayout.solver.widgets.WidgetContainer, androidx.constraintlayout.solver.widgets.ConstraintWidget
    public void reset() {
        this.mSystem.reset();
        this.mPaddingLeft = 0;
        this.mPaddingRight = 0;
        this.mPaddingTop = 0;
        this.mPaddingBottom = 0;
        this.mWidgetGroups.clear();
        this.mSkipSolver = false;
        super.reset();
    }

    public boolean isWidthMeasuredTooSmall() {
        return this.mWidthMeasuredTooSmall;
    }

    public boolean isHeightMeasuredTooSmall() {
        return this.mHeightMeasuredTooSmall;
    }

    public boolean addChildrenToSolver(LinearSystem system) {
        addToSolver(system);
        int count = this.mChildren.size();
        for (int i = 0; i < count; i++) {
            ConstraintWidget widget = this.mChildren.get(i);
            if (widget instanceof ConstraintWidgetContainer) {
                ConstraintWidget.DimensionBehaviour horizontalBehaviour = widget.mListDimensionBehaviors[0];
                ConstraintWidget.DimensionBehaviour verticalBehaviour = widget.mListDimensionBehaviors[1];
                if (horizontalBehaviour == ConstraintWidget.DimensionBehaviour.WRAP_CONTENT) {
                    widget.setHorizontalDimensionBehaviour(ConstraintWidget.DimensionBehaviour.FIXED);
                }
                if (verticalBehaviour == ConstraintWidget.DimensionBehaviour.WRAP_CONTENT) {
                    widget.setVerticalDimensionBehaviour(ConstraintWidget.DimensionBehaviour.FIXED);
                }
                widget.addToSolver(system);
                if (horizontalBehaviour == ConstraintWidget.DimensionBehaviour.WRAP_CONTENT) {
                    widget.setHorizontalDimensionBehaviour(horizontalBehaviour);
                }
                if (verticalBehaviour == ConstraintWidget.DimensionBehaviour.WRAP_CONTENT) {
                    widget.setVerticalDimensionBehaviour(verticalBehaviour);
                }
            } else {
                Optimizer.checkMatchParent(this, system, widget);
                widget.addToSolver(system);
            }
        }
        int i2 = this.mHorizontalChainsSize;
        if (i2 > 0) {
            Chain.applyChainConstraints(this, system, 0);
        }
        if (this.mVerticalChainsSize > 0) {
            Chain.applyChainConstraints(this, system, 1);
        }
        return USE_SNAPSHOT;
    }

    public void updateChildrenFromSolver(LinearSystem system, boolean[] flags) {
        flags[2] = false;
        updateFromSolver(system);
        int count = this.mChildren.size();
        for (int i = 0; i < count; i++) {
            ConstraintWidget widget = this.mChildren.get(i);
            widget.updateFromSolver(system);
            if (widget.mListDimensionBehaviors[0] == ConstraintWidget.DimensionBehaviour.MATCH_CONSTRAINT && widget.getWidth() < widget.getWrapWidth()) {
                flags[2] = USE_SNAPSHOT;
            }
            if (widget.mListDimensionBehaviors[1] == ConstraintWidget.DimensionBehaviour.MATCH_CONSTRAINT && widget.getHeight() < widget.getWrapHeight()) {
                flags[2] = USE_SNAPSHOT;
            }
        }
    }

    public void setPadding(int left, int top, int right, int bottom) {
        this.mPaddingLeft = left;
        this.mPaddingTop = top;
        this.mPaddingRight = right;
        this.mPaddingBottom = bottom;
    }

    public void setRtl(boolean isRtl) {
        this.mIsRtl = isRtl;
    }

    public boolean isRtl() {
        return this.mIsRtl;
    }

    @Override // androidx.constraintlayout.solver.widgets.ConstraintWidget
    public void analyze(int optimizationLevel) {
        super.analyze(optimizationLevel);
        int count = this.mChildren.size();
        for (int i = 0; i < count; i++) {
            this.mChildren.get(i).analyze(optimizationLevel);
        }
    }

    /* JADX WARN: Removed duplicated region for block: B:115:0x028d  */
    /* JADX WARN: Removed duplicated region for block: B:118:0x02aa  */
    /* JADX WARN: Removed duplicated region for block: B:120:0x02ba  */
    /* JADX WARN: Removed duplicated region for block: B:133:0x0300  */
    /* JADX WARN: Removed duplicated region for block: B:76:0x019b  */
    /* JADX WARN: Removed duplicated region for block: B:77:0x01a3  */
    /* JADX WARN: Removed duplicated region for block: B:94:0x01f2  */
    @Override // androidx.constraintlayout.solver.widgets.WidgetContainer
    /*
        Code decompiled incorrectly, please refer to instructions dump.
    */
    public void layout() {
        int groupSize;
        boolean wrap_override;
        int groupSize2;
        boolean needsSolving;
        boolean z;
        boolean needsSolving2;
        int count;
        int width;
        int height;
        int prex = this.mX;
        int prey = this.mY;
        int prew = Math.max(0, getWidth());
        int preh = Math.max(0, getHeight());
        this.mWidthMeasuredTooSmall = false;
        this.mHeightMeasuredTooSmall = false;
        if (this.mParent != null) {
            if (this.mSnapshot == null) {
                this.mSnapshot = new Snapshot(this);
            }
            this.mSnapshot.updateFrom(this);
            setX(this.mPaddingLeft);
            setY(this.mPaddingTop);
            resetAnchors();
            resetSolverVariables(this.mSystem.getCache());
        } else {
            this.mX = 0;
            this.mY = 0;
        }
        int i = 32;
        if (this.mOptimizationLevel != 0) {
            if (!optimizeFor(8)) {
                optimizeReset();
            }
            if (!optimizeFor(32)) {
                optimize();
            }
            this.mSystem.graphOptimizer = USE_SNAPSHOT;
        } else {
            this.mSystem.graphOptimizer = false;
        }
        boolean wrap_override2 = false;
        ConstraintWidget.DimensionBehaviour originalVerticalDimensionBehaviour = this.mListDimensionBehaviors[1];
        ConstraintWidget.DimensionBehaviour originalHorizontalDimensionBehaviour = this.mListDimensionBehaviors[0];
        resetChains();
        if (this.mWidgetGroups.size() == 0) {
            this.mWidgetGroups.clear();
            this.mWidgetGroups.add(0, new ConstraintWidgetGroup(this.mChildren));
        }
        int groupSize3 = this.mWidgetGroups.size();
        List<ConstraintWidget> allChildren = this.mChildren;
        boolean hasWrapContent = (getHorizontalDimensionBehaviour() == ConstraintWidget.DimensionBehaviour.WRAP_CONTENT || getVerticalDimensionBehaviour() == ConstraintWidget.DimensionBehaviour.WRAP_CONTENT) ? USE_SNAPSHOT : false;
        int groupIndex = 0;
        while (groupIndex < groupSize3 && !this.mSkipSolver) {
            if (this.mWidgetGroups.get(groupIndex).mSkipSolver) {
                groupSize = groupSize3;
            } else {
                if (optimizeFor(i)) {
                    if (getHorizontalDimensionBehaviour() != ConstraintWidget.DimensionBehaviour.FIXED || getVerticalDimensionBehaviour() != ConstraintWidget.DimensionBehaviour.FIXED) {
                        this.mChildren = (ArrayList) this.mWidgetGroups.get(groupIndex).mConstrainedGroup;
                    } else {
                        this.mChildren = (ArrayList) this.mWidgetGroups.get(groupIndex).getWidgetsToSolve();
                    }
                }
                resetChains();
                int count2 = this.mChildren.size();
                int countSolve = 0;
                int i2 = 0;
                while (i2 < count2) {
                    ConstraintWidget widget = this.mChildren.get(i2);
                    int countSolve2 = countSolve;
                    if (widget instanceof WidgetContainer) {
                        ((WidgetContainer) widget).layout();
                    }
                    i2++;
                    countSolve = countSolve2;
                }
                int countSolve3 = countSolve;
                boolean needsSolving3 = USE_SNAPSHOT;
                boolean wrap_override3 = wrap_override2;
                while (needsSolving3) {
                    int countSolve4 = countSolve3 + 1;
                    try {
                        this.mSystem.reset();
                        resetChains();
                        createObjectVariables(this.mSystem);
                        int i3 = 0;
                        while (i3 < count2) {
                            boolean needsSolving4 = needsSolving3;
                            try {
                                wrap_override = wrap_override3;
                            } catch (Exception e) {
                                e = e;
                                wrap_override = wrap_override3;
                                needsSolving3 = needsSolving4;
                            }
                            try {
                                this.mChildren.get(i3).createObjectVariables(this.mSystem);
                                i3++;
                                needsSolving3 = needsSolving4;
                                wrap_override3 = wrap_override;
                            } catch (Exception e2) {
                                e = e2;
                                needsSolving3 = needsSolving4;
                                e.printStackTrace();
                                PrintStream printStream = System.out;
                                needsSolving = needsSolving3;
                                StringBuilder sb = new StringBuilder();
                                groupSize2 = groupSize3;
                                sb.append("EXCEPTION : ");
                                sb.append(e);
                                printStream.println(sb.toString());
                                if (needsSolving) {
                                }
                                boolean needsSolving5 = false;
                                if (hasWrapContent) {
                                }
                                needsSolving2 = false;
                                count = count2;
                                wrap_override3 = wrap_override;
                                width = Math.max(this.mMinWidth, getWidth());
                                if (width > getWidth()) {
                                }
                                height = Math.max(this.mMinHeight, getHeight());
                                if (height > getHeight()) {
                                }
                                if (wrap_override3) {
                                }
                                countSolve3 = countSolve4;
                                groupSize3 = groupSize2;
                                count2 = count;
                            }
                        }
                        wrap_override = wrap_override3;
                        needsSolving3 = addChildrenToSolver(this.mSystem);
                        if (needsSolving3) {
                            try {
                                this.mSystem.minimize();
                            } catch (Exception e3) {
                                e = e3;
                                e.printStackTrace();
                                PrintStream printStream2 = System.out;
                                needsSolving = needsSolving3;
                                StringBuilder sb2 = new StringBuilder();
                                groupSize2 = groupSize3;
                                sb2.append("EXCEPTION : ");
                                sb2.append(e);
                                printStream2.println(sb2.toString());
                                if (needsSolving) {
                                }
                                boolean needsSolving52 = false;
                                if (hasWrapContent) {
                                }
                                needsSolving2 = false;
                                count = count2;
                                wrap_override3 = wrap_override;
                                width = Math.max(this.mMinWidth, getWidth());
                                if (width > getWidth()) {
                                }
                                height = Math.max(this.mMinHeight, getHeight());
                                if (height > getHeight()) {
                                }
                                if (wrap_override3) {
                                }
                                countSolve3 = countSolve4;
                                groupSize3 = groupSize2;
                                count2 = count;
                            }
                        }
                        needsSolving = needsSolving3;
                        groupSize2 = groupSize3;
                    } catch (Exception e4) {
                        e = e4;
                        wrap_override = wrap_override3;
                    }
                    if (needsSolving) {
                        updateChildrenFromSolver(this.mSystem, Optimizer.flags);
                    } else {
                        updateFromSolver(this.mSystem);
                        int i4 = 0;
                        while (true) {
                            if (i4 >= count2) {
                                break;
                            }
                            ConstraintWidget widget2 = this.mChildren.get(i4);
                            if (widget2.mListDimensionBehaviors[0] != ConstraintWidget.DimensionBehaviour.MATCH_CONSTRAINT) {
                                z = USE_SNAPSHOT;
                            } else if (widget2.getWidth() >= widget2.getWrapWidth()) {
                                z = USE_SNAPSHOT;
                            } else {
                                Optimizer.flags[2] = USE_SNAPSHOT;
                                break;
                            }
                            if (widget2.mListDimensionBehaviors[z ? 1 : 0] != ConstraintWidget.DimensionBehaviour.MATCH_CONSTRAINT || widget2.getHeight() >= widget2.getWrapHeight()) {
                                i4++;
                            } else {
                                Optimizer.flags[2] = z;
                                break;
                            }
                        }
                    }
                    boolean needsSolving522 = false;
                    if (hasWrapContent || countSolve4 >= 8 || !Optimizer.flags[2]) {
                        needsSolving2 = false;
                        count = count2;
                        wrap_override3 = wrap_override;
                    } else {
                        int maxY = 0;
                        int maxX = 0;
                        int maxX2 = 0;
                        while (maxX2 < count2) {
                            boolean needsSolving6 = needsSolving522;
                            ConstraintWidget widget3 = this.mChildren.get(maxX2);
                            maxX = Math.max(maxX, widget3.mX + widget3.getWidth());
                            maxY = Math.max(maxY, widget3.mY + widget3.getHeight());
                            maxX2++;
                            needsSolving522 = needsSolving6;
                            count2 = count2;
                        }
                        needsSolving2 = needsSolving522;
                        count = count2;
                        int maxX3 = Math.max(this.mMinWidth, maxX);
                        int maxY2 = Math.max(this.mMinHeight, maxY);
                        if (originalHorizontalDimensionBehaviour == ConstraintWidget.DimensionBehaviour.WRAP_CONTENT && getWidth() < maxX3) {
                            setWidth(maxX3);
                            this.mListDimensionBehaviors[0] = ConstraintWidget.DimensionBehaviour.WRAP_CONTENT;
                            wrap_override3 = USE_SNAPSHOT;
                            needsSolving2 = true;
                        } else {
                            wrap_override3 = wrap_override;
                        }
                        if (originalVerticalDimensionBehaviour == ConstraintWidget.DimensionBehaviour.WRAP_CONTENT && getHeight() < maxY2) {
                            setHeight(maxY2);
                            this.mListDimensionBehaviors[1] = ConstraintWidget.DimensionBehaviour.WRAP_CONTENT;
                            wrap_override3 = USE_SNAPSHOT;
                            needsSolving2 = true;
                        }
                    }
                    width = Math.max(this.mMinWidth, getWidth());
                    if (width > getWidth()) {
                        setWidth(width);
                        this.mListDimensionBehaviors[0] = ConstraintWidget.DimensionBehaviour.FIXED;
                        wrap_override3 = USE_SNAPSHOT;
                        needsSolving2 = USE_SNAPSHOT;
                    }
                    height = Math.max(this.mMinHeight, getHeight());
                    if (height > getHeight()) {
                        setHeight(height);
                        this.mListDimensionBehaviors[1] = ConstraintWidget.DimensionBehaviour.FIXED;
                        wrap_override3 = USE_SNAPSHOT;
                        needsSolving2 = USE_SNAPSHOT;
                    }
                    if (wrap_override3) {
                        needsSolving3 = needsSolving2;
                    } else {
                        if (this.mListDimensionBehaviors[0] == ConstraintWidget.DimensionBehaviour.WRAP_CONTENT && prew > 0 && getWidth() > prew) {
                            this.mWidthMeasuredTooSmall = USE_SNAPSHOT;
                            wrap_override3 = USE_SNAPSHOT;
                            this.mListDimensionBehaviors[0] = ConstraintWidget.DimensionBehaviour.FIXED;
                            setWidth(prew);
                            needsSolving2 = USE_SNAPSHOT;
                        }
                        if (this.mListDimensionBehaviors[1] == ConstraintWidget.DimensionBehaviour.WRAP_CONTENT && preh > 0 && getHeight() > preh) {
                            this.mHeightMeasuredTooSmall = USE_SNAPSHOT;
                            wrap_override3 = USE_SNAPSHOT;
                            this.mListDimensionBehaviors[1] = ConstraintWidget.DimensionBehaviour.FIXED;
                            setHeight(preh);
                            needsSolving3 = true;
                        } else {
                            needsSolving3 = needsSolving2;
                        }
                    }
                    countSolve3 = countSolve4;
                    groupSize3 = groupSize2;
                    count2 = count;
                }
                groupSize = groupSize3;
                this.mWidgetGroups.get(groupIndex).updateUnresolvedWidgets();
                wrap_override2 = wrap_override3;
            }
            groupIndex++;
            groupSize3 = groupSize;
            i = 32;
        }
        this.mChildren = (ArrayList) allChildren;
        if (this.mParent != null) {
            int width2 = Math.max(this.mMinWidth, getWidth());
            int height2 = Math.max(this.mMinHeight, getHeight());
            this.mSnapshot.applyTo(this);
            setWidth(this.mPaddingLeft + width2 + this.mPaddingRight);
            setHeight(this.mPaddingTop + height2 + this.mPaddingBottom);
        } else {
            this.mX = prex;
            this.mY = prey;
        }
        if (wrap_override2) {
            this.mListDimensionBehaviors[0] = originalHorizontalDimensionBehaviour;
            this.mListDimensionBehaviors[1] = originalVerticalDimensionBehaviour;
        }
        resetSolverVariables(this.mSystem.getCache());
        if (this == getRootConstraintContainer()) {
            updateDrawPosition();
        }
    }

    public void preOptimize() {
        optimizeReset();
        analyze(this.mOptimizationLevel);
    }

    public void solveGraph() {
        ResolutionAnchor leftNode = getAnchor(ConstraintAnchor.Type.LEFT).getResolutionNode();
        ResolutionAnchor topNode = getAnchor(ConstraintAnchor.Type.TOP).getResolutionNode();
        leftNode.resolve(null, 0.0f);
        topNode.resolve(null, 0.0f);
    }

    public void resetGraph() {
        ResolutionAnchor leftNode = getAnchor(ConstraintAnchor.Type.LEFT).getResolutionNode();
        ResolutionAnchor topNode = getAnchor(ConstraintAnchor.Type.TOP).getResolutionNode();
        leftNode.invalidateAnchors();
        topNode.invalidateAnchors();
        leftNode.resolve(null, 0.0f);
        topNode.resolve(null, 0.0f);
    }

    public void optimizeForDimensions(int width, int height) {
        if (this.mListDimensionBehaviors[0] != ConstraintWidget.DimensionBehaviour.WRAP_CONTENT && this.mResolutionWidth != null) {
            this.mResolutionWidth.resolve(width);
        }
        if (this.mListDimensionBehaviors[1] != ConstraintWidget.DimensionBehaviour.WRAP_CONTENT && this.mResolutionHeight != null) {
            this.mResolutionHeight.resolve(height);
        }
    }

    public void optimizeReset() {
        int count = this.mChildren.size();
        resetResolutionNodes();
        for (int i = 0; i < count; i++) {
            this.mChildren.get(i).resetResolutionNodes();
        }
    }

    public void optimize() {
        if (!optimizeFor(8)) {
            analyze(this.mOptimizationLevel);
        }
        solveGraph();
    }

    public boolean handlesInternalConstraints() {
        return false;
    }

    public ArrayList<Guideline> getVerticalGuidelines() {
        ArrayList<Guideline> guidelines = new ArrayList<>();
        int mChildrenSize = this.mChildren.size();
        for (int i = 0; i < mChildrenSize; i++) {
            ConstraintWidget widget = this.mChildren.get(i);
            if (widget instanceof Guideline) {
                Guideline guideline = (Guideline) widget;
                if (guideline.getOrientation() == 1) {
                    guidelines.add(guideline);
                }
            }
        }
        return guidelines;
    }

    public ArrayList<Guideline> getHorizontalGuidelines() {
        ArrayList<Guideline> guidelines = new ArrayList<>();
        int mChildrenSize = this.mChildren.size();
        for (int i = 0; i < mChildrenSize; i++) {
            ConstraintWidget widget = this.mChildren.get(i);
            if (widget instanceof Guideline) {
                Guideline guideline = (Guideline) widget;
                if (guideline.getOrientation() == 0) {
                    guidelines.add(guideline);
                }
            }
        }
        return guidelines;
    }

    public LinearSystem getSystem() {
        return this.mSystem;
    }

    private void resetChains() {
        this.mHorizontalChainsSize = 0;
        this.mVerticalChainsSize = 0;
    }

    void addChain(ConstraintWidget constraintWidget, int type) {
        if (type == 0) {
            addHorizontalChain(constraintWidget);
        } else if (type == 1) {
            addVerticalChain(constraintWidget);
        }
    }

    private void addHorizontalChain(ConstraintWidget widget) {
        int i = this.mHorizontalChainsSize + 1;
        ChainHead[] chainHeadArr = this.mHorizontalChainsArray;
        if (i >= chainHeadArr.length) {
            this.mHorizontalChainsArray = (ChainHead[]) Arrays.copyOf(chainHeadArr, chainHeadArr.length * 2);
        }
        this.mHorizontalChainsArray[this.mHorizontalChainsSize] = new ChainHead(widget, 0, isRtl());
        this.mHorizontalChainsSize++;
    }

    private void addVerticalChain(ConstraintWidget widget) {
        int i = this.mVerticalChainsSize + 1;
        ChainHead[] chainHeadArr = this.mVerticalChainsArray;
        if (i >= chainHeadArr.length) {
            this.mVerticalChainsArray = (ChainHead[]) Arrays.copyOf(chainHeadArr, chainHeadArr.length * 2);
        }
        this.mVerticalChainsArray[this.mVerticalChainsSize] = new ChainHead(widget, 1, isRtl());
        this.mVerticalChainsSize++;
    }

    public List<ConstraintWidgetGroup> getWidgetGroups() {
        return this.mWidgetGroups;
    }
}
